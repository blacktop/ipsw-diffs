## NFUIService

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/XPCServices/NFUIService.xpc/NFUIService`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x4c68
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x5a0
+364.20.0.0.0
+  __TEXT.__text: 0x4798
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x208
-  __TEXT.__cstring: 0x7be
-  __TEXT.__oslogstring: 0x3d2
+  __TEXT.__cstring: 0x747
+  __TEXT.__oslogstring: 0x300
   __TEXT.__swift5_typeref: 0xa7
   __TEXT.__objc_methname: 0x5cd
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_builtin: 0x14
+  __TEXT.__objc_classname: 0xd6
+  __TEXT.__objc_methtype: 0x277
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__objc_classname: 0xa8
-  __TEXT.__objc_methtype: 0x231
-  __TEXT.__unwind_info: 0x138
-  __DATA_CONST.__auth_got: 0x388
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__const: 0x238
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x1f0
   __DATA.__data: 0x250
-  __DATA.__bss: 0x1a0
   __DATA.__common: 0x18
+  __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3F76C3F5-261D-365C-AA5F-FD3C47BE982F
+  UUID: 7C2E96B4-99AB-3EF7-B6FD-88CAF5B6F4E6
   Functions: 69
-  Symbols:   197
-  CStrings:  219
+  Symbols:   189
+  CStrings:  225
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retain
+ _objc_retain_x22
+ _objc_retain_x25
- __swift_FORCE_LOAD_$_swiftAccelerate
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x23
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x8
- _object_getClass
- _object_getClassName
- _sel_getName
CStrings:
+ "%s:%i Controller has not been activated"
+ "%s:%i Couldn't create notification! %d"
+ "%s:%i Error : Re-using the sharing service..."
+ "%s:%i Got message %@ for context %@"
+ "%s:%i Invalid parameter"
+ "%s:%i Invalidation already requested."
+ "%s:%i Invalidation handler received with error %@ using context %@"
+ "%s:%i Launched to %@ error %@"
+ "%s:%i Launching %{public}@, reason=%lu, domain=%lu"
+ "%s:%i Posting user notification"
+ "%s:%i Received notification response %d (error %d)"
+ "%s:%i Unknown action %@"
+ "%s:%i Unknown action for context %@"
+ "%s:%i Update mode on next activation"
+ "%{public}s:%i Controller has not been activated"
+ "%{public}s:%i Couldn't create notification! %d"
+ "%{public}s:%i Error : Re-using the sharing service..."
+ "%{public}s:%i Got message %@ for context %@"
+ "%{public}s:%i Invalid parameter"
+ "%{public}s:%i Invalidation already requested."
+ "%{public}s:%i Invalidation handler received with error %@ using context %@"
+ "%{public}s:%i Launched to %@ error %@"
+ "%{public}s:%i Launching %{public}@, reason=%lu, domain=%lu"
+ "%{public}s:%i Posting user notification"
+ "%{public}s:%i Received notification response %d (error %d)"
+ "%{public}s:%i Unknown action %@"
+ "%{public}s:%i Unknown action for context %@"
+ "%{public}s:%i Update mode on next activation"
+ "-[NFServiceCoreNFCUI activate:context:withCompletion:]"
+ "-[NFServiceCoreNFCUI activate:context:withCompletion:]_block_invoke"
+ "-[NFServiceCoreNFCUI setUIMode:]"
+ "-[NFServiceCoreNFCUI setUIOperationMode:]"
+ "-[NFServiceCoreNFCUI tagCount:]"
+ "-[NFUIServiceServer runService:callback:]"
+ "-[NFUIServiceServer showPaymentSessionGotoSettingsPrompt:]"
- "%c[%{public}s %{public}s]:%i Controller has not been activated"
- "%c[%{public}s %{public}s]:%i Couldn't create notification! %d"
- "%c[%{public}s %{public}s]:%i Error : Re-using the sharing service..."
- "%c[%{public}s %{public}s]:%i Got message %@ for context %@"
- "%c[%{public}s %{public}s]:%i Invalid parameter"
- "%c[%{public}s %{public}s]:%i Invalidation already requested."
- "%c[%{public}s %{public}s]:%i Invalidation handler received with error %@ using context %@"
- "%c[%{public}s %{public}s]:%i Launched to %@ error %@"
- "%c[%{public}s %{public}s]:%i Launching %{public}@, reason=%lu, domain=%lu"
- "%c[%{public}s %{public}s]:%i Posting user notification"
- "%c[%{public}s %{public}s]:%i Received notification response %d (error %d)"
- "%c[%{public}s %{public}s]:%i Unknown action %@"
- "%c[%{public}s %{public}s]:%i Unknown action for context %@"
- "%c[%{public}s %{public}s]:%i Update mode on next activation"

```
