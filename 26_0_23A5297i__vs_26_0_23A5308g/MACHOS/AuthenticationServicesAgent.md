## AuthenticationServicesAgent

> `/usr/libexec/AuthenticationServicesAgent`

```diff

-7622.1.19.10.4
-  __TEXT.__text: 0x1de90
+7622.1.21.10.3
+  __TEXT.__text: 0x1e778
   __TEXT.__auth_stubs: 0x1520
   __TEXT.__objc_stubs: 0x1e20
   __TEXT.__objc_methlist: 0x9b4
-  __TEXT.__cstring: 0xa38
+  __TEXT.__cstring: 0xcc8
   __TEXT.__const: 0x3d2
   __TEXT.__objc_methname: 0x3534
-  __TEXT.__oslogstring: 0xa61
+  __TEXT.__oslogstring: 0xa91
   __TEXT.__objc_classname: 0xc1
   __TEXT.__objc_methtype: 0xe89
   __TEXT.__gcc_except_tab: 0x14c

   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__eh_frame: 0x680
   __DATA_CONST.__auth_got: 0xaa0
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x180
-  __DATA_CONST.__const: 0xac0
+  __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 11E5245E-DA2D-3056-93C0-E43DB9BAF68E
-  Functions: 433
+  UUID: 07AEA79F-BF83-3D70-BF27-C7F0043F1DB8
+  Functions: 455
   Symbols:   561
-  CStrings:  634
+  CStrings:  647
 
CStrings:
+ "-[PublicKeyCredentialOperation hasSelectedAssertion]_block_invoke"
+ "-[PublicKeyCredentialOperation hasTornDown]_block_invoke"
+ "-[PublicKeyCredentialOperation mergeIdentifiersToAssertionResponses:]_block_invoke"
+ "-[PublicKeyCredentialOperation selectPlatformAssertion:]_block_invoke"
+ "-[PublicKeyCredentialOperation selectSecurityKeyAssertion:]_block_invoke"
+ "-[PublicKeyCredentialOperation setPlatformAssertionSelectionCallback:]_block_invoke"
+ "-[PublicKeyCredentialOperation setSecurityKeyAssertionSelectionCallback:]_block_invoke"
+ "-[PublicKeyCredentialOperation tearDownIfNecessary]_block_invoke"
+ "?"
+ "@\"_WKWebAuthenticationAssertionResponse\""
+ "Unexpected semaphore timeout in %{public}s"

```
