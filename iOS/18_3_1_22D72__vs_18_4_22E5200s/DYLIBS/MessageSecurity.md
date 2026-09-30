## MessageSecurity

> `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

```diff

-115.80.1.0.0
-  __TEXT.__text: 0x3c03c
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x1b00
-  __TEXT.__const: 0xd64
-  __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__cstring: 0x35fd
-  __TEXT.__oslogstring: 0xa5c
+115.100.9.0.0
+  __TEXT.__text: 0x3ca68
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x1ce4
+  __TEXT.__const: 0x13b4
+  __TEXT.__gcc_except_tab: 0x834
+  __TEXT.__cstring: 0x351d
+  __TEXT.__oslogstring: 0xabc
   __TEXT.__swift5_typeref: 0x2a8
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x3f0

   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x1088
-  __TEXT.__eh_frame: 0x958
+  __TEXT.__unwind_info: 0x1098
+  __TEXT.__eh_frame: 0x978
   __TEXT.__objc_classname: 0x2b3
-  __TEXT.__objc_methname: 0x3fb9
-  __TEXT.__objc_methtype: 0x1726
+  __TEXT.__objc_methname: 0x4037
+  __TEXT.__objc_methtype: 0x1791
   __TEXT.__objc_stubs: 0x2840
   __DATA_CONST.__got: 0x378
   __DATA_CONST.__const: 0x44e8

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe00
+  __DATA_CONST.__objc_selrefs: 0xea0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__auth_ptr: 0xb8
-  __AUTH_CONST.__const: 0x1460
+  __AUTH_CONST.__const: 0x1480
   __AUTH_CONST.__cfstring: 0x24e0
-  __AUTH_CONST.__objc_const: 0x4230
+  __AUTH_CONST.__objc_const: 0x3ee8
   __DATA.__objc_ivar: 0x1ac
-  __DATA.__data: 0x1170
+  __DATA.__data: 0x1160
   __DATA.__bss: 0x5a0
   __DATA.__common: 0x2711
   __DATA_DIRTY.__objc_data: 0xb10

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1928
-  Symbols:   2416
-  CStrings:  1295
+  Functions: 2012
+  Symbols:   2555
+  CStrings:  1294
 
Symbols:
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initializeBufferWithCopyOfBuffer
- _objc_retain_x28
- _objc_retain_x9
CStrings:
+ "-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]"
+ "@40@0:8^{__SecCertificate=}16@24^{__SecIdentity=}32"
+ "@48@0:8^{__SecCertificate=}16@24@32^{__SecIdentity=}40"
+ "MSCMSRecipientInfo requires an originator identity for an EC recipient. Encode will fail if not set."
+ "initWithCertificate:algorithmCapabilities:originator:"
+ "initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:"
- "-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:]"
- "Fatal error"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Integers.swift"
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"

```
