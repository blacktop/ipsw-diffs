## managedeventsd

> `/usr/libexec/managedeventsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-113.0.2.0.0
-  __TEXT.__text: 0x23a70
-  __TEXT.__auth_stubs: 0xce0
+113.1.9.0.0
+  __TEXT.__text: 0x23d98
+  __TEXT.__auth_stubs: 0xd00
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x6d4
-  __TEXT.__const: 0x870
+  __TEXT.__const: 0x880
   __TEXT.__objc_methname: 0x192b
-  __TEXT.__cstring: 0x1142
+  __TEXT.__cstring: 0x11bc
   __TEXT.__objc_classname: 0x195
   __TEXT.__objc_methtype: 0x22ce
-  __TEXT.__oslogstring: 0xeb2
+  __TEXT.__oslogstring: 0xf32
   __TEXT.__gcc_except_tab: 0x1004
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x163

   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0xb40
+  __TEXT.__unwind_info: 0xb38
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0xce0
   __DATA_CONST.__cfstring: 0x760

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__auth_got: 0x690
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0xa0
   __DATA.__objc_const: 0x1b78
   __DATA.__objc_selrefs: 0x508
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x360
-  __DATA.__data: 0x418
+  __DATA.__data: 0x408
   __DATA.__bss: 0x210
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 649
-  Symbols:   296
-  CStrings:  511
+  Functions: 648
+  Symbols:   297
+  CStrings:  515
 
Symbols:
+ _$sSS14validatingUTF8SSSgSPys4Int8VG_tcfC
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
- _$sSSSysMc
- _$sSy10FoundationE8containsySbqd__SyRd__lF
CStrings:
+ "Failed to obtain notify name from event"
+ "Ignoring unrecognized notify name: %{public}s"
+ "Notification"
+ "Received notifyd notification: %{public}s (event key: %{public}s)"
+ "Unexpected XPC event type on notifyd stream"
+ "com.apple.RemoteManagement.diskManagementSettingsChanged"
+ "com.apple.RemoteManagement.launchRestrictionSettingsChanged"
- "Failed to obtain notification name"
- "Received notifyd notification: %s"
- "launchRestriction"
```
