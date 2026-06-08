## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2969.120.2.0.0
-  __TEXT.__text: 0x12d98
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x2580
-  __TEXT.__objc_methlist: 0xc74
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x36cb
-  __TEXT.__objc_methname: 0x2dfb
-  __TEXT.__objc_classname: 0x197
-  __TEXT.__objc_methtype: 0x629
+3033.0.0.0.0
+  __TEXT.__text: 0x11c48
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_methlist: 0xc8c
+  __TEXT.__const: 0x2f2
+  __TEXT.__cstring: 0x373b
+  __TEXT.__objc_methname: 0x2e2b
+  __TEXT.__objc_classname: 0x187
+  __TEXT.__objc_methtype: 0x639
   __TEXT.__oslogstring: 0x2466
-  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__gcc_except_tab: 0x2b4
   __TEXT.__constg_swiftt: 0x12c
-  __TEXT.__swift5_typeref: 0x78
+  __TEXT.__swift5_typeref: 0x70
   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3c0
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x738
   __DATA_CONST.__cfstring: 0xf00
   __DATA_CONST.__objc_classlist: 0x78

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x588
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x1400
-  __DATA.__objc_selrefs: 0xc70
+  __DATA.__objc_selrefs: 0xc80
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0x4e0
-  __DATA.__data: 0x298
+  __DATA.__data: 0x290
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B015AFF4-CCED-36B7-90B5-064FE73B052F
-  Functions: 324
-  Symbols:   292
-  CStrings:  1216
+  UUID: 3F3ED9B3-2CF2-30E1-82D0-AE04EF846439
+  Functions: 327
+  Symbols:   295
+  CStrings:  1223
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _swift_release_x20
+ _swift_release_x8
+ _swift_retain_x20
- _swift_release
- _swift_retain
CStrings:
+ "-[MBSuspendingClock clockByAddingPositiveTimeInterval:]"
+ "@24@0:8Q16"
+ "@24@0:8d16"
+ "MBSuspendingClock.m"
+ "_initWithStartTime:"
+ "clockByAddingPositiveTimeInterval:"
+ "interval >= 0"

```
