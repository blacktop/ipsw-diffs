## askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
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
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-130.0.25.0.0
-  __TEXT.__text: 0x514dc
-  __TEXT.__auth_stubs: 0x1360
-  __TEXT.__objc_stubs: 0x5860
-  __TEXT.__objc_methlist: 0x2944
-  __TEXT.__const: 0x650
-  __TEXT.__cstring: 0x3254
+130.0.29.0.0
+  __TEXT.__text: 0x51954
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_stubs: 0x58a0
+  __TEXT.__objc_methlist: 0x295c
+  __TEXT.__const: 0x660
+  __TEXT.__cstring: 0x3274
   __TEXT.__objc_classname: 0x61b
-  __TEXT.__objc_methname: 0x6d26
-  __TEXT.__oslogstring: 0x57b8
+  __TEXT.__objc_methname: 0x6d66
+  __TEXT.__oslogstring: 0x5880
   __TEXT.__objc_methtype: 0x16f9
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__swift5_typeref: 0x2c7

   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0x70
-  __TEXT.__unwind_info: 0xc40
+  __TEXT.__unwind_info: 0xc50
   __TEXT.__eh_frame: 0xb88
-  __DATA_CONST.__const: 0x18f8
-  __DATA_CONST.__cfstring: 0x3080
+  __DATA_CONST.__const: 0x1948
+  __DATA_CONST.__cfstring: 0x30e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x9c0
+  __DATA_CONST.__auth_got: 0x9d0
   __DATA_CONST.__got: 0x588
   __DATA_CONST.__auth_ptr: 0x150
   __DATA.__objc_const: 0x5608
-  __DATA.__objc_selrefs: 0x19e8
+  __DATA.__objc_selrefs: 0x19f8
   __DATA.__objc_ivar: 0x360
   __DATA.__objc_data: 0x1490
   __DATA.__data: 0x680

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1150
-  Symbols:   545
-  CStrings:  2128
+  Functions: 1154
+  Symbols:   547
+  CStrings:  2136
 
Symbols:
+ _CGContextScaleCTM
+ _CGContextTranslateCTM
CStrings:
+ "%{public}@: %@ (%@) Kill Switch: %d"
+ "%{public}@: AskTo Kill Switch ON *or* FeatureFlag disabled - Checking if we can send via PeopleClient"
+ "AskTo"
+ "Bag is NIL when checking %@ (%@) kill switch - defaulting to allow"
+ "Completion Handler is NIL when checking %@ (%@) kill switch - ATB request won't be sent"
+ "Messages"
+ "Unhandled kill switch type: %ld - defaulting to allow"
+ "_checkKillSwitch:completionHandler:"
+ "_sendViaAskToFramework:"
+ "enable-ks-via-askto"
- "%{public}@: AskToIntegration Feature Flag disabled - Checking if we can send via PeopleClient"
- "%{public}@: canSendViaMessages: %d - kill switch: %d"
```
