from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class MemoryAgent:
    logs: List[Dict] = field(default_factory=list)
    max_len: int = 30

    def store(self, sender, message, weight=1):
        self.logs.append({
            "sender": sender,
            "message": message,
            "weight": weight,
            "timestamp": datetime.utcnow().isoformat()
        })
        self._prune()

    def _prune(self):
        if len(self.logs) > self.max_len:
            self.logs = sorted(
                self.logs,
                key=lambda x: (x["weight"], x["timestamp"]),
                reverse=True
            )[:self.max_len]

    def context(self, n=5):
        return " | ".join(
            f"{m['sender']}: {m['message']}" for m in self.logs[-n:]
        )
