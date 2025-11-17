## MobilePhone

> `/Applications/MobilePhone.app/MobilePhone`

```diff

-3027.300.31.2.2
-  __TEXT.__text: 0x1d80a8
-  __TEXT.__auth_stubs: 0x4850
+3027.300.41.2.1
+  __TEXT.__text: 0x1d8330
+  __TEXT.__auth_stubs: 0x4860
   __TEXT.__objc_stubs: 0x19820
-  __TEXT.__objc_methlist: 0x10610
+  __TEXT.__objc_methlist: 0x10640
   __TEXT.__const: 0x7b5c
-  __TEXT.__objc_methname: 0x2b929
-  __TEXT.__cstring: 0xcbba
-  __TEXT.__oslogstring: 0xb776
+  __TEXT.__objc_methname: 0x2b9fb
+  __TEXT.__cstring: 0xcbda
+  __TEXT.__oslogstring: 0xb856
   __TEXT.__objc_classname: 0x18c1
-  __TEXT.__objc_methtype: 0x6aa8
+  __TEXT.__objc_methtype: 0x6aab
   __TEXT.__gcc_except_tab: 0xc8c
   __TEXT.__dlopen_cstrs: 0x5e
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_protos: 0x40
   __TEXT.__unwind_info: 0x7e58
   __TEXT.__eh_frame: 0x9544
-  __DATA_CONST.__auth_got: 0x2438
+  __DATA_CONST.__auth_got: 0x2440
   __DATA_CONST.__got: 0x1880
   __DATA_CONST.__auth_ptr: 0x1320
-  __DATA_CONST.__const: 0xa328
+  __DATA_CONST.__const: 0xa348
   __DATA_CONST.__cfstring: 0x4f20
   __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0xb8

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x19200
-  __DATA.__objc_selrefs: 0x93b0
-  __DATA.__objc_ivar: 0xc0c
+  __DATA.__objc_const: 0x19260
+  __DATA.__objc_selrefs: 0x93d0
+  __DATA.__objc_ivar: 0xc14
   __DATA.__objc_data: 0x6ab0
   __DATA.__data: 0x7378
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x5c48
+  __DATA.__bss: 0x5c58
   __DATA.__common: 0x8d8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 28D02AA3-E89E-3B48-834E-E54001013C77
-  Functions: 11214
-  Symbols:   77729
-  CStrings:  10166
+  UUID: DE2637A2-9E8D-3B81-BF06-16F50E61F2B2
+  Functions: 11220
+  Symbols:   77768
+  CStrings:  10179
 
Symbols:
+ +[PHVoicemailNavigationController badge].cold.1
+ -[MPVoicemailController contactUpdateNeeded]
+ -[MPVoicemailController metadataCacheUpdateNeeded]
+ -[MPVoicemailController setContactUpdateNeeded:]
+ -[MPVoicemailController setMetadataCacheUpdateNeeded:]
+ GCC_except_table27
+ OBJC_IVAR_$_MPVoicemailController._contactUpdateNeeded
+ OBJC_IVAR_$_MPVoicemailController._metadataCacheUpdateNeeded
+ __40+[PHVoicemailNavigationController badge]_block_invoke.111
+ __40+[PHVoicemailNavigationController badge]_block_invoke.119
+ __40+[PHVoicemailNavigationController badge]_block_invoke.125
+ __40+[PHVoicemailNavigationController badge]_block_invoke.125.cold.1
+ __40+[PHVoicemailNavigationController badge]_block_invoke.126
+ __40+[PHVoicemailNavigationController badge]_block_invoke.126.cold.1
+ __40+[PHVoicemailNavigationController badge]_block_invoke.128
+ ___PHVoicemailNavigationControllerBadgeQueue
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ badge.onceToken
- GCC_except_table26
- GCC_except_table35
- __40+[PHVoicemailNavigationController badge]_block_invoke.115
- __40+[PHVoicemailNavigationController badge]_block_invoke.120
- __40+[PHVoicemailNavigationController badge]_block_invoke.121
- __40+[PHVoicemailNavigationController badge]_block_invoke.121.cold.1
- __40+[PHVoicemailNavigationController badge]_block_invoke.122
- __40+[PHVoicemailNavigationController badge]_block_invoke.122.cold.1
- __block_literal_global.118
CStrings:
+ "%@ skipping redundant contact update - one already queued"
+ "%@ skipping redundant metadata cache update - one already queued"
+ "+[VoicemailNavigationController badge] %{public}@ skipping - badge was updated by another operation"
+ "AB"
+ "TAB,N,V_contactUpdateNeeded"
+ "TAB,N,V_metadataCacheUpdateNeeded"
+ "_contactUpdateNeeded"
+ "_metadataCacheUpdateNeeded"
+ "com.apple.mobilephone.voicemail.badge"
+ "contactUpdateNeeded"
+ "metadataCacheUpdateNeeded"
+ "setContactUpdateNeeded:"
+ "setMetadataCacheUpdateNeeded:"

```
