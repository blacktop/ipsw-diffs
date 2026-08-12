## PhoneKit

> `/System/Library/PrivateFrameworks/PhoneKit.framework/PhoneKit`

```diff

-147.100.5.2.1
-  __TEXT.__text: 0x19d04
-  __TEXT.__objc_methlist: 0x10d4
+153.100.1.2.7
+  __TEXT.__text: 0x19f40
+  __TEXT.__objc_methlist: 0x110c
   __TEXT.__const: 0x754
-  __TEXT.__cstring: 0x993
+  __TEXT.__cstring: 0x9b3
   __TEXT.__oslogstring: 0xf23
   __TEXT.__gcc_except_tab: 0x174
   __TEXT.__ustring: 0x4

   __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_reflstr: 0x3
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__unwind_info: 0x680
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x520
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11c0
+  __DATA_CONST.__objc_selrefs: 0x11f0
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x3b0
-  __AUTH_CONST.__const: 0x1c8
-  __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__objc_const: 0x16e8
+  __DATA_CONST.__got: 0x3c0
+  __AUTH_CONST.__const: 0x1e8
+  __AUTH_CONST.__cfstring: 0xce0
+  __AUTH_CONST.__objc_const: 0x1778
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH.__objc_data: 0x70
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH.__objc_data: 0xc0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0xb8
   __DATA.__data: 0x3a0
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x68
   __DATA_DIRTY.__bss: 0xe0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 524
-  Symbols:   1478
-  CStrings:  189
+  Functions: 530
+  Symbols:   1499
+  CStrings:  191
 
Symbols:
+ -[PHBootSession getBootSessionUUID]
+ -[PHBootSession isInDifferentBootSession]
+ -[PHBootSession lastKnownBootSessionID]
+ -[PHBootSession persistBootSessionID]
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_PHBootSession
+ _OBJC_METACLASS_$_PHBootSession
+ _PHLastBootUUIDKey
+ _TUBundleIdentifierMobilePhoneApplication
+ __OBJC_$_INSTANCE_METHODS_PHBootSession
+ __OBJC_CLASS_RO_$_PHBootSession
+ __OBJC_METACLASS_RO_$_PHBootSession
+ ___35-[PHBootSession getBootSessionUUID]_block_invoke
+ _getBootSessionUUID.bootUUID
+ _getBootSessionUUID.onceToken
+ _objc_msgSend$UUIDString
+ _objc_msgSend$getBootSessionUUID
+ _objc_msgSend$lastKnownBootSessionID
+ _objc_msgSend$stringWithUTF8String:
+ _objc_opt_new
+ _sysctlbyname
CStrings:
+ "PHLastBootUUIDKey"
+ "kern.bootsessionuuid"
```
