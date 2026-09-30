## nfcd

> `/usr/libexec/nfcd`

```diff

-364.24.0.0.0
-  __TEXT.__text: 0x1f06bc
+365.2.0.0.0
+  __TEXT.__text: 0x1f0d74
   __TEXT.__auth_stubs: 0x17b0
   __TEXT.__delay_stubs: 0x500
   __TEXT.__delay_helper: 0x16f4
-  __TEXT.__objc_stubs: 0xd3e0
-  __TEXT.__objc_methlist: 0x9b30
+  __TEXT.__objc_stubs: 0xd400
+  __TEXT.__objc_methlist: 0x9b40
   __TEXT.__const: 0x1384
-  __TEXT.__objc_methname: 0x1499d
-  __TEXT.__cstring: 0x21a07
-  __TEXT.__objc_classname: 0x1d50
-  __TEXT.__objc_methtype: 0x4dc1
-  __TEXT.__oslogstring: 0x1f23c
-  __TEXT.__unwind_info: 0x2db0
+  __TEXT.__objc_methname: 0x14985
+  __TEXT.__cstring: 0x21a91
+  __TEXT.__objc_classname: 0x1d80
+  __TEXT.__objc_methtype: 0x4df2
+  __TEXT.__oslogstring: 0x1f323
+  __TEXT.__unwind_info: 0x2dc8
   __DATA_CONST.__auth_got: 0xc80
   __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__auth_ptr: 0x18

   __DATA_CONST.__cfstring: 0x11540
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x388
+  __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1e8
-  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_intobj: 0x77d0
   __DATA_CONST.__objc_arraydata: 0x1d30
   __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_dictobj: 0xf28
-  __DATA.__objc_const: 0x147b8
+  __DATA.__objc_const: 0x147e8
   __DATA.__objc_selrefs: 0x4868
-  __DATA.__objc_ivar: 0x10a0
+  __DATA.__objc_ivar: 0x10a4
   __DATA.__objc_data: 0x3d40
-  __DATA.__data: 0x2b34
+  __DATA.__data: 0x2b94
   __DATA.__bss: 0x288
   __DATA.__common: 0x12
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F3878BD-F8AB-3627-A398-699310F6906B
-  Functions: 4158
+  UUID: 63D2E997-1572-3768-9CEA-F9725AB0E511
+  Functions: 4162
   Symbols:   585
-  CStrings:  13578
+  CStrings:  13587
 
CStrings:
+ "%{public}s:%i %{public}@, mode=%lu"
+ "%{public}s:%i AID=%{public}@ selection is not allowed"
+ "%{public}s:%i Default contactless app update: domain=%lu"
+ "%{public}s:%i Invalid parameter, %{public}@"
+ "%{public}s:%i Managed channel instruction, %{public}@"
+ "%{public}s:%i Requested applet not found, %{public}@"
+ "%{public}s:%i aid=%{public}@, data=%{public}@"
+ "-[_NFCredentialSession handleSecureElementTransactionData:appletIdentifier:]"
+ "-[_NFHardwareManager(FieldDetect) domainUpdate:]_block_invoke"
+ "@\"NSObject<NFWalletPresentationServiceDelegate>\""
+ "NFCD built from (B&I) Stockholm_Base-365.2"
+ "NFWalletPresentationServiceDelegate"
+ "Routing failure: %{public}@"
+ "domainUpdate:"
- "%{public}s:%i %@, mode=%lu"
- "%{public}s:%i AID=%@ selection is not allowed"
- "%{public}s:%i Select command not supported: %@"
- "NFCD built from (B&I) Stockholm_Base-364.24"
- "Routing failure: %@"
- "automaticallyNotifiesObserversForKey:"

```
