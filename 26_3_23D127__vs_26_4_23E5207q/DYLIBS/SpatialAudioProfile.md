## SpatialAudioProfile

> `/System/Library/PrivateFrameworks/SpatialAudioProfile.framework/SpatialAudioProfile`

```diff

-33.1.0.0.0
-  __TEXT.__text: 0xda8
-  __TEXT.__auth_stubs: 0x1e0
+34.25.1.1.1
+  __TEXT.__text: 0xe6c
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__cstring: 0x332
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x9d
   __TEXT.__objc_methname: 0x3de
   __TEXT.__objc_methtype: 0x119

   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__auth_got: 0xf0
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x340
   __AUTH.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DCBF1EB-46F9-3A53-AE8A-D4D9F96758C4
+  UUID: 07A4309C-8F45-31BB-96A4-C2D1AB83D9D4
   Functions: 42
-  Symbols:   201
+  Symbols:   199
   CStrings:  94
 
Symbols:
+ _objc_release_x2
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
- _objc_claimAutoreleasedReturnValue
- _objc_release_x1
- _objc_retain
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[SpatialAudioProfileClient init] : 100 -> 108
~ -[SpatialAudioProfileClient fetchSpatialAudioProfileRecordWithCompletion:] : 152 -> 160
~ ___75-[SpatialAudioProfileClient _fetchSpatialAudioProfileRecordWithCompletion:]_block_invoke : 164 -> 156
~ -[SpatialAudioProfileClient _ensureXPCStarted] : 376 -> 384
~ -[SpatialAudioProfileClient setDispatchQueue:] : 12 -> 64
~ -[SpatialAudioProfileRecord encodeWithCoder:] : 128 -> 136
~ -[SpatialAudioProfileRecord initWithCoder:] : 180 -> 188
~ -[SpatialAudioProfileRecord description] : 108 -> 116
~ -[SpatialAudioProfileRecord setProfileData:] : 12 -> 64
~ -[SpatialAudioProfileRecord setProfileURL:] : 12 -> 64

```
