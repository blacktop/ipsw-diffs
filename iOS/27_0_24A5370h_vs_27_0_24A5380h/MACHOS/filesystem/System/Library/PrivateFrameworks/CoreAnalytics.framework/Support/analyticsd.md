## analyticsd

> `/System/Library/PrivateFrameworks/CoreAnalytics.framework/Support/analyticsd`

```diff

-  __TEXT.__text: 0x1338d0
+  __TEXT.__text: 0x1338fc
   __TEXT.__auth_stubs: 0x1e10
   __TEXT.__objc_stubs: 0x2c00
   __TEXT.__init_offsets: 0x24
   __TEXT.__objc_methlist: 0xb9c
-  __TEXT.__gcc_except_tab: 0x14558
+  __TEXT.__gcc_except_tab: 0x14564
   __TEXT.__const: 0xa9b4
-  __TEXT.__cstring: 0x153e9
-  __TEXT.__oslogstring: 0x1ace1
+  __TEXT.__cstring: 0x154cb
+  __TEXT.__oslogstring: 0x1adf9
   __TEXT.__objc_methname: 0x2f28
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1879

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x7d60
+  __TEXT.__unwind_info: 0x7d68
   __TEXT.__eh_frame: 0x398
   __DATA_CONST.__const: 0xac88
   __DATA_CONST.__cfstring: 0xd00

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6043
+  Functions: 6046
   Symbols:   726
-  CStrings:  4150
+  CStrings:  4154
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
CStrings:
+ "CREATE INDEX IF NOT EXISTS IX_modify_eventdefs_modify_event_name ON modify_eventdefs(modify_event_name); CREATE INDEX IF NOT EXISTS IX_config_modify_eventdefs_modify_eventdef_id ON config_modify_eventdefs(modify_eventdef_id);"
+ "[Config Store] DATABASE INITIALIZATION: modifying for V12 schema - restoring modify-event lookup indices dropped in V9"
+ "[Config Store] ERROR: Failed to restore modify-eventdef lookup indices; %s"
+ "[Config Store] ERROR: Failed to restore modify-eventdef lookup indices[null database]"

```
