## askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Versions/Current/Resources/askpermissiond`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-130.0.25.0.0
-  __TEXT.__text: 0x361e4
+130.0.29.0.0
+  __TEXT.__text: 0x3667c
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x45a0
-  __TEXT.__objc_methlist: 0x27d0
-  __TEXT.__const: 0x2a6
-  __TEXT.__cstring: 0x1cd8
+  __TEXT.__objc_stubs: 0x45e0
+  __TEXT.__objc_methlist: 0x27e8
+  __TEXT.__const: 0x2b6
+  __TEXT.__cstring: 0x1cf8
   __TEXT.__objc_classname: 0x4e0
-  __TEXT.__objc_methname: 0x6119
-  __TEXT.__oslogstring: 0x3afb
+  __TEXT.__objc_methname: 0x6159
+  __TEXT.__oslogstring: 0x3bc3
   __TEXT.__objc_methtype: 0x150a
   __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__swift5_typeref: 0x134

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__unwind_info: 0x8d8
   __TEXT.__eh_frame: 0x398
-  __DATA_CONST.__const: 0x1080
-  __DATA_CONST.__cfstring: 0x2760
+  __DATA_CONST.__const: 0x10e0
+  __DATA_CONST.__cfstring: 0x27c0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0x53b0
-  __DATA.__objc_selrefs: 0x1630
+  __DATA.__objc_selrefs: 0x1640
   __DATA.__objc_ivar: 0x364
   __DATA.__objc_data: 0x11b8
   __DATA.__data: 0x460

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 924
+  Functions: 928
   Symbols:   258
-  CStrings:  1750
+  CStrings:  1758
 
CStrings:
+ "%{public}@: %@ (%@) Kill Switch: %d"
+ "%{public}@: AskTo Kill Switch ON *or* FeatureFlag disabled - Checking if we can send via PeopleClient"
+ "04:22:04"
+ "AskTo"
+ "Aug 10 2026"
+ "Bag is NIL when checking %@ (%@) kill switch - defaulting to allow"
+ "Completion Handler is NIL when checking %@ (%@) kill switch - ATB request won't be sent"
+ "Messages"
+ "Unhandled kill switch type: %ld - defaulting to allow"
+ "_checkKillSwitch:completionHandler:"
+ "_sendViaAskToFramework:"
+ "enable-ks-via-askto"
- "%{public}@: AskToIntegration Feature Flag disabled - Checking if we can send via PeopleClient"
- "%{public}@: canSendViaMessages: %d - kill switch: %d"
- "00:58:13"
- "Jul 11 2026"
```
