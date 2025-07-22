## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-493.0.0.0.0
-  __TEXT.__text: 0x124604
-  __TEXT.__auth_stubs: 0x1ae0
+496.0.0.0.0
+  __TEXT.__text: 0x126334
+  __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0xa04
-  __TEXT.__cstring: 0x12ef9
-  __TEXT.__const: 0xaf1d
-  __TEXT.__gcc_except_tab: 0x127c4
-  __TEXT.__oslogstring: 0x16cad
+  __TEXT.__cstring: 0x13270
+  __TEXT.__const: 0xaf3d
+  __TEXT.__gcc_except_tab: 0x129e8
+  __TEXT.__oslogstring: 0x1722c
   __TEXT.__objc_classname: 0x168
   __TEXT.__objc_methtype: 0x143b
   __TEXT.__objc_methname: 0x2885
-  __TEXT.__unwind_info: 0x7500
-  __DATA_CONST.__auth_got: 0xd88
+  __TEXT.__unwind_info: 0x75b0
+  __DATA_CONST.__auth_got: 0xd98
   __DATA_CONST.__got: 0x5d0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xacc0
+  __DATA_CONST.__const: 0xad58
   __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0F218005-B410-344D-BAA6-CA909917EDD1
-  Functions: 5627
-  Symbols:   646
-  CStrings:  3768
+  UUID: 27E9C3C9-3AD1-3168-8D1A-52416AE93937
+  Functions: 5670
+  Symbols:   648
+  CStrings:  3800
 
Symbols:
+ _sqlite3_expanded_sql
+ _sqlite3_free
CStrings:
+ "\n      ALTER TABLE agg_session\n      ADD COLUMN is_active BOOLEAN DEFAULT 1\n    "
+ " UPDATE transform_metadata SET rollover_session_id=?1 WHERE agg_session_id IN (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?2); UPDATE transform_states SET rollover_session_id=?1 WHERE transform_metadata_id IN (SELECT transform_metadata_id FROM transform_metadata WHERE agg_session_id IN (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?2));"
+ "CONFIG HEADER: %s"
+ "CONFIG UUID: %s"
+ "DELETE FROM agg_session WHERE agg_session_period=?1 AND is_active = 0 AND agg_session_id NOT IN (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?1 ORDER BY agg_session_start_timestamp DESC LIMIT 1);"
+ "DELETE FROM agg_session WHERE is_active = 0"
+ "DELETE FROM agg_session WHERE is_active = 0 AND agg_session_end_boundary <= ?1"
+ "DELETE FROM agg_session WHERE is_active = 0 AND agg_session_period = ?1"
+ "DELETE FROM transform_metadata WHERE rollover_session_id=?1 AND agg_session_id IN (SELECT agg_session_id FROM agg_session WHERE agg_session_period = ?2 AND is_active = 0)"
+ "DELETE FROM transform_states WHERE rollover_session_id=?1 AND transform_metadata_id IN (SELECT tm.transform_metadata_id FROM transform_metadata AS tm JOIN agg_session ON tm.agg_session_id = agg_session.agg_session_id WHERE agg_session.agg_session_period = ?2 AND is_active = 0)"
+ "INSERT INTO transform_metadata (transform_uuid, transform_type, transform_budget_used, transform_event_count, rollover_session_id, agg_session_id) VALUES (?1, ?2, ?3, ?4, ?5, (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?6 ORDER BY agg_session_start_timestamp ASC LIMIT 1)) ON CONFLICT(transform_uuid, rollover_session_id) DO UPDATE SET transform_budget_used=?3, transform_event_count=?4 WHERE transform_uuid=?1 AND rollover_session_id=?5"
+ "NEW Rollover Session ID: %s"
+ "Rollover Session ID: %s"
+ "UPDATE agg_session SET is_active = 0"
+ "UPDATE agg_session SET is_active = 0 WHERE agg_session_end_boundary <= ?1"
+ "UPDATE agg_session SET is_active = 0 WHERE agg_session_period = ?1"
+ "[ClientManager] === Tasking notification received with taskingId: %{public}s! Locating and storing (but not activating) new configurations"
+ "[Platform] ERROR: Failed to get hw.memsize"
+ "[State Store] Error preparing database mark-agg-sessions-inactive; %s"
+ "[State Store] Error preparing database mark-agg-sessions-inactive[null database]"
+ "[State Store] Error preparing database mark-all-agg-sessions-inactive; %s"
+ "[State Store] Error preparing database mark-all-agg-sessions-inactive[null database]"
+ "[State Store] Error preparing database mark-expired-agg-sessions-inactive; %s"
+ "[State Store] Error preparing database mark-expired-agg-sessions-inactive[null database]"
+ "[State Store] Error preparing database remove-all-inactive-agg-sessions; %s"
+ "[State Store] Error preparing database remove-all-inactive-agg-sessions[null database]"
+ "[State Store] Error preparing database remove-expired-agg-sessions; %s"
+ "[State Store] Error preparing database remove-expired-agg-sessions[null database]"
+ "[State Store] Error preparing database remove-inactive-agg-sessions-for-period; %s"
+ "[State Store] Error preparing database remove-inactive-agg-sessions-for-period[null database]"
+ "[State Store] Error preparing database remove-old-agg-sessions; %s"
+ "[State Store] Error preparing database remove-old-agg-sessions[null database]"
+ "[State Store] Failed to add is_active column to agg_session; %s"
+ "[State Store] Failed to add is_active column to agg_session[null database]"
+ "[State Store] Failed to mark agg_session inactive; %s"
+ "[State Store] Failed to mark agg_session inactive[null database]"
+ "[State Store] Failed to mark all agg_sessions inactive; %s"
+ "[State Store] Failed to mark all agg_sessions inactive[null database]"
+ "[State Store] Failed to mark expired agg_sessions inactive; %s"
+ "[State Store] Failed to mark expired agg_sessions inactive[null database]"
+ "[State Store] Failed to remove all inactive agg_sessions; %s"
+ "[State Store] Failed to remove all inactive agg_sessions[null database]"
+ "[State Store] Failed to remove expired agg_sessions; %s"
+ "[State Store] Failed to remove expired agg_sessions[null database]"
+ "[State Store] Failed to remove inactive agg_sessions for period; %s"
+ "[State Store] Failed to remove inactive agg_sessions for period[null database]"
+ "[State Store] Failed to update transforms rollover session id; %s"
+ "[State Store] Failed to update transforms rollover session id[null database]"
- "DELETE FROM agg_session"
- "DELETE FROM transform_metadata WHERE rollover_session_id=?1 AND agg_session_id IN (SELECT agg_session_id FROM agg_session WHERE agg_session_period = ?1)"
- "DELETE FROM transform_states WHERE rollover_session_id=?1 AND transform_metadata_id IN (SELECT tm.transform_metadata_id FROM transform_metadata AS tm JOIN agg_session ON tm.agg_session_id = agg_session.agg_session_id WHERE agg_session.agg_session_period = ?2)"
- "INSERT INTO transform_metadata (transform_uuid, transform_type, transform_budget_used, transform_event_count, rollover_session_id, agg_session_id) VALUES (?1, ?2, ?3, ?4, ?5, (SELECT COALESCE((SELECT agg_session_id FROM agg_session WHERE agg_session_period=?6 AND agg_session_start_timestamp<=?7 ORDER BY agg_session_start_timestamp ASC LIMIT 1), (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?6 ORDER BY agg_session_start_timestamp ASC LIMIT 1)))) ON CONFLICT(transform_uuid, rollover_session_id) DO UPDATE SET transform_budget_used=?3, transform_event_count=?4 WHERE transform_uuid=?1 AND rollover_session_id=?5"
- "[ClientManager] === Tasking notification recieved with taskingId: %{public}s! Locating and storing (but not activating) new configurations"
- "[Platform] ERROR: Failed to get hw.memezise"
- "[State Store] Error preparing database remove-all-agg-sessions; %s"
- "[State Store] Error preparing database remove-all-agg-sessions[null database]"
- "[State Store] Failed to create transaction for reinitializing all aggregation sessions; %s"
- "[State Store] Failed to create transaction for reinitializing all aggregation sessions[null database]"
- "[State Store] Failed to create transaction for removing and recreating expired aggregation sessions; %s"
- "[State Store] Failed to create transaction for removing and recreating expired aggregation sessions[null database]"
- "[State Store] Failed to create transaction for replacing expired aggregation sessions; %s"
- "[State Store] Failed to create transaction for replacing expired aggregation sessions[null database]"
- "[State Store] Failed to remove all agg_sessions; %s"
- "[State Store] Failed to remove all agg_sessions[null database]"

```
