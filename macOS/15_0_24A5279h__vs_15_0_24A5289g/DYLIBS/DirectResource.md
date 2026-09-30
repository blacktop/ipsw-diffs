## DirectResource

> `/System/Library/PrivateFrameworks/DirectResource.framework/Versions/A/DirectResource`

```diff

-7.0.4.0.0
-  __TEXT.__text: 0x1a6d8
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__cstring: 0x537
+7.0.6.0.0
+  __TEXT.__text: 0x1b49c
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__cstring: 0x55d
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0x158
   __TEXT.__unwind_info: 0x60
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x304
+  __TEXT.__objc_methname: 0x315
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x148
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0xc90
+  __DATA_CONST.__objc_selrefs: 0x158
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0xd10
   __AUTH_CONST.__cfstring: 0x60
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 807
-  Symbols:   280
-  CStrings:  94
+  Functions: 844
+  Symbols:   284
+  CStrings:  99
 
Symbols:
+ _DRCommitQueueEntryGetUserPayload
+ _DRContextCommitAddFence
+ _DRContextGetCommitUserPayload
+ _DRContextSetCommitUserPayload
+ _DRFenceCreate
+ _DRFenceGetLabel
+ _DRFenceInvalidate
+ _DRResourcesCommitGetUserPayload
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
- _DRCommitQueueEntryGetUserFlags
- _DRCommitQueueEntryGetUserIdentifier
- _DRContextSetCommitUserFlags
- _DRContextSetCommitUserIdentifier
- _DRResourcesCommitGetUserFlags
- _DRResourcesCommitGetUserIdentifier
CStrings:
+ "!m_active"
+ "CommandBuffer %!p(MISSING)"
+ "DirectFence.cpp"
+ "Fence: "
+ "invalidate"
+ "m_active"
+ "userPayload"
+ "~DirectFence"
- "\tUser Identifier=%!l(MISSING)lu Flags=%!l(MISSING)lu"
- "userFlags"
- "userIdentifier"

```
