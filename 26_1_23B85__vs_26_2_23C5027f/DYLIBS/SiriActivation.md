## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3505.22.1.11.1
-  __TEXT.__text: 0x4f1cc
+3510.4.2.0.0
+  __TEXT.__text: 0x4f468
   __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x6064
+  __TEXT.__objc_methlist: 0x607c
   __TEXT.__const: 0x838
-  __TEXT.__cstring: 0xa0fd
+  __TEXT.__cstring: 0xa14d
   __TEXT.__oslogstring: 0x6e87
   __TEXT.__gcc_except_tab: 0xe5c
   __TEXT.__dlopen_cstrs: 0x1bc

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1600
+  __TEXT.__unwind_info: 0x1608
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x101d
-  __TEXT.__objc_methname: 0xddc0
-  __TEXT.__objc_methtype: 0x23b0
-  __TEXT.__objc_stubs: 0x95a0
+  __TEXT.__objc_methname: 0xde24
+  __TEXT.__objc_methtype: 0x23c9
+  __TEXT.__objc_stubs: 0x95c0
   __DATA_CONST.__got: 0x6a8
   __DATA_CONST.__const: 0x1670
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e18
+  __DATA_CONST.__objc_selrefs: 0x2e28
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x530

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 175D8654-5C98-3DEF-9F9D-BD9535B6BDBD
-  Functions: 2171
-  Symbols:   7435
-  CStrings:  4551
+  UUID: E1BEED92-0CED-3D23-860B-EEA80B383692
+  Functions: 2173
+  Symbols:   7440
+  CStrings:  4556
 
Symbols:
+ +[SASPresentationDecision activationPresentationForPresentationIdentifiers:source:]
+ +[SASPresentationDecision activationPresentationForPresentationIdentifiers:source:].cold.1
+ -[SASPresentationManager _presentationsLock_nextPresentationToActivateForSource:]
+ -[SASPresentationManager nextPresentationToActivateForSource:]
+ GCC_except_table61
+ _objc_msgSend$_presentationsLock_nextPresentationToActivateForSource:
+ _objc_msgSend$activationPresentationForPresentationIdentifiers:source:
+ _objc_msgSend$nextPresentationToActivateForSource:
- +[SASPresentationDecision activationPresentationForPresentationIdentifiers:]
- +[SASPresentationDecision activationPresentationForPresentationIdentifiers:].cold.1
- GCC_except_table57
- _objc_msgSend$activationPresentationForPresentationIdentifiers:
- _objc_msgSend$nextPresentationToActivate
CStrings:
+ "+[SASPresentationDecision activationPresentationForPresentationIdentifiers:source:]"
+ "-[SASPresentationManager nextPresentationToActivateForSource:]"
+ "_presentationsLock_nextPresentationToActivateForSource:"
+ "activationPresentationForPresentationIdentifiers:source:"
+ "nextPresentationToActivateForSource:"
+ "q24@0:8Q16"
+ "q32@0:8@16Q24"
- "+[SASPresentationDecision activationPresentationForPresentationIdentifiers:]"
- "activationPresentationForPresentationIdentifiers:"

```
