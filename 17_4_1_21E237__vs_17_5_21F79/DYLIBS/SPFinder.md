## SPFinder

> `/System/Library/PrivateFrameworks/SPFinder.framework/SPFinder`

```diff

-358.16.0.2.0
-  __TEXT.__text: 0x87d4
+360.20.0.1.0
+  __TEXT.__text: 0x8a88
   __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0xbf8
-  __TEXT.__cstring: 0x85f
+  __TEXT.__objc_methlist: 0xc90
+  __TEXT.__cstring: 0x88f
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__oslogstring: 0x673

   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x38
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3e4
   __TEXT.__eh_frame: 0x1b8
-  __TEXT.__objc_classname: 0x22e
-  __TEXT.__objc_methname: 0x18f6
-  __TEXT.__objc_methtype: 0x625
-  __TEXT.__objc_stubs: 0x1080
+  __TEXT.__objc_classname: 0x23e
+  __TEXT.__objc_methname: 0x19d6
+  __TEXT.__objc_methtype: 0x652
+  __TEXT.__objc_stubs: 0x10c0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x290
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x19f0
-  __DATA_CONST.__objc_selrefs: 0x588
+  __DATA_CONST.__objc_const: 0x1ac0
+  __DATA_CONST.__objc_selrefs: 0x5c0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__cfstring: 0x7c0
-  __AUTH_CONST.__objc_const: 0x798
+  __DATA_CONST.__objc_superrefs: 0x58
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0x828
   __AUTH_CONST.__const: 0x1e8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x380
-  __AUTH.__objc_data: 0x1f0
+  __AUTH.__objc_data: 0x240
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x4b8
   __DATA.__bss: 0x210
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 338
-  Symbols:   1146
-  CStrings:  531
+  Functions: 349
+  Symbols:   1183
+  CStrings:  549
 
Symbols:
+ +[SPPublishResult supportsSecureCoding]
+ -[SPAdvertisement isPosh]
+ -[SPAdvertisement setIsPosh:]
+ -[SPPublishResult .cxx_destruct]
+ -[SPPublishResult aaaPubKeyHash]
+ -[SPPublishResult encodeWithCoder:]
+ -[SPPublishResult initWithCoder:]
+ -[SPPublishResult initWithRequestUUID:aaaPubKeyHash:]
+ -[SPPublishResult requestUUID]
+ -[SPPublishResult setAaaPubKeyHash:]
+ -[SPPublishResult setRequestUUID:]
+ _OBJC_CLASS_$_SPPublishResult
+ _OBJC_IVAR_$_SPAdvertisement._isPosh
+ _OBJC_IVAR_$_SPPublishResult._aaaPubKeyHash
+ _OBJC_IVAR_$_SPPublishResult._requestUUID
+ _OBJC_METACLASS_$_SPPublishResult
+ __OBJC_$_CLASS_METHODS_SPPublishResult
+ __OBJC_$_CLASS_PROP_LIST_SPPublishResult
+ __OBJC_$_INSTANCE_METHODS_SPPublishResult
+ __OBJC_$_INSTANCE_VARIABLES_SPPublishResult
+ __OBJC_$_PROP_LIST_SPPublishResult
+ __OBJC_CLASS_PROTOCOLS_$_SPPublishResult
+ __OBJC_CLASS_RO_$_SPPublishResult
+ __OBJC_METACLASS_RO_$_SPPublishResult
+ _objc_msgSend$isPosh
+ _objc_msgSend$setIsPosh:
CStrings:
+ "SPAdvertisement %@%@ %@ posh: %i"
+ "SPPublishResult"
+ "T@\"NSData\",C,N,V_aaaPubKeyHash"
+ "T@\"NSUUID\",C,N,V_requestUUID"
+ "TB,N,V_isPosh"
+ "_aaaPubKeyHash"
+ "_isPosh"
+ "_requestUUID"
+ "aaaPubKeyHash"
+ "initWithRequestUUID:aaaPubKeyHash:"
+ "isPosh"
+ "requestUUID"
+ "setAaaPubKeyHash:"
+ "setIsPosh:"
+ "setRequestUUID:"
+ "v24@0:8@?<v@?@\"SPPublishResult\"@\"NSError\">16"
- "SPAdvertisement %@%@ %@"

```
