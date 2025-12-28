import time
from perception.sensor_ingest import ingest_sensor
from gatekeeper.entity_filter import entity_filter
from gatekeeper.intent_filter import intent_filter
from agents.claim_state import ClaimState
from editorial.decision_engine import editorial_decision

claim = ClaimState()

event = ingest_sensor("TEMP_01", 120)

if entity_filter(event) and intent_filter(event):
    claim.verify(event)

decision = editorial_decision(claim.status)
print("Decision:", decision)
