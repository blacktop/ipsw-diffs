## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-496.2.1.0.0
+496.2.2.0.0
   __TEXT.__text: 0x126334
   __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0xa04
-  __TEXT.__cstring: 0x13273
+  __TEXT.__cstring: 0x13285
   __TEXT.__const: 0xaf3d
   __TEXT.__gcc_except_tab: 0x129e8
   __TEXT.__oslogstring: 0x1722c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6D2590E2-EF36-34CE-9219-4ED9CB6DF6E0
+  UUID: A9D42F83-BDAA-3016-937B-0ED29141F473
   Functions: 5670
   Symbols:   648
   CStrings:  3800
CStrings:
+ "INSERT INTO transform_metadata (transform_uuid, transform_type, transform_budget_used, transform_event_count, rollover_session_id, agg_session_id) VALUES (?1, ?2, ?3, ?4, ?5, (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?6 AND is_active = 1 ORDER BY agg_session_start_timestamp ASC LIMIT 1)) ON CONFLICT(transform_uuid, rollover_session_id) DO UPDATE SET transform_budget_used=?3, transform_event_count=?4 WHERE transform_uuid=?1 AND rollover_session_id=?5"
- "INSERT INTO transform_metadata (transform_uuid, transform_type, transform_budget_used, transform_event_count, rollover_session_id, agg_session_id) VALUES (?1, ?2, ?3, ?4, ?5, (SELECT agg_session_id FROM agg_session WHERE agg_session_period=?6 ORDER BY agg_session_start_timestamp ASC LIMIT 1)) ON CONFLICT(transform_uuid, rollover_session_id) DO UPDATE SET transform_budget_used=?3, transform_event_count=?4 WHERE transform_uuid=?1 AND rollover_session_id=?5"

```
