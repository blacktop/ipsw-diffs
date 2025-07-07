## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-489.0.0.0.0
-  __TEXT.__text: 0x123e8c
+493.0.0.0.0
+  __TEXT.__text: 0x124604
   __TEXT.__auth_stubs: 0x1ae0
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0xa04
-  __TEXT.__cstring: 0x12ef0
+  __TEXT.__cstring: 0x12ef9
   __TEXT.__const: 0xaf1d
-  __TEXT.__gcc_except_tab: 0x12764
-  __TEXT.__oslogstring: 0x16c1b
+  __TEXT.__gcc_except_tab: 0x127c4
+  __TEXT.__oslogstring: 0x16cad
   __TEXT.__objc_classname: 0x168
   __TEXT.__objc_methtype: 0x143b
   __TEXT.__objc_methname: 0x2885
-  __TEXT.__unwind_info: 0x74e8
+  __TEXT.__unwind_info: 0x7500
   __DATA_CONST.__auth_got: 0xd88
   __DATA_CONST.__got: 0x5d0
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 50323E67-1AC1-3D30-A2B3-7EDB19A386BA
-  Functions: 5622
+  UUID: 0F218005-B410-344D-BAA6-CA909917EDD1
+  Functions: 5627
   Symbols:   646
-  CStrings:  3765
+  CStrings:  3768
 
CStrings:
+ "SELECT DISTINCT transform_uuid, transform_def, derived_sampling_perc, transform_started_aggregating_timestamp FROM enabled_transforms_by_event_view WHERE event_name=?1;"
+ "[Config Load] %s"
+ "[Config Load] no parent config candidate present to load for tasked config."
+ "[Config Load] parent uuid does not match base config"
- "SELECT transform_uuid, transform_def, derived_sampling_perc, transform_started_aggregating_timestamp FROM enabled_transforms_by_event_view WHERE event_name=?1;"

```
