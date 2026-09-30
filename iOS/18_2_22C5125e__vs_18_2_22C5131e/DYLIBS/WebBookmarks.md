## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-620.1.14.10.4
+620.1.15.10.3
   __TEXT.__text: 0x9c0e8
   __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0x749c
   __TEXT.__const: 0x2b0
   __TEXT.__gcc_except_tab: 0xac0c
-  __TEXT.__cstring: 0xdb6a
+  __TEXT.__cstring: 0xdb88
   __TEXT.__oslogstring: 0x7613
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__unwind_info: 0x4030
CStrings:
+ "INSERT INTO windows (active_tab_group_id, active_profile_id, date_closed, extra_attributes, is_last_session, local_tab_group_id, private_tab_group_id, scene_id, uuid) VALUES (?, ?, ?, ?, 1, ?, ?, ?, ?) ON CONFLICT (uuid) DO UPDATE SET active_tab_group_id = excluded.active_tab_group_id, active_profile_id = excluded.active_profile_id, date_closed = excluded.date_closed, extra_attributes = excluded.extra_attributes, local_tab_group_id = excluded.local_tab_group_id, private_tab_group_id = excluded.private_tab_group_id, is_last_session = 1, scene_id = excluded.scene_id"
- "INSERT INTO windows (active_tab_group_id, active_profile_id, date_closed, extra_attributes, is_last_session, local_tab_group_id, private_tab_group_id, scene_id, uuid) VALUES (?, ?, ?, ?, 1, ?, ?, ?, ?) ON CONFLICT (uuid) DO UPDATE SET active_tab_group_id = excluded.active_tab_group_id, active_profile_id = excluded.active_profile_id, date_closed = excluded.date_closed, extra_attributes = excluded.extra_attributes, local_tab_group_id = excluded.local_tab_group_id, private_tab_group_id = excluded.private_tab_group_id, is_last_session = 1"

```
