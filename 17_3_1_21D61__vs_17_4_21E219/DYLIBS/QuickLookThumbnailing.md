## QuickLookThumbnailing

> `/System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing`

```diff

-186.4.1.0.0
-  __TEXT.__text: 0x2b524
+186.5.3.0.0
+  __TEXT.__text: 0x2b6ec
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x2c04
+  __TEXT.__objc_methlist: 0x2c14
   __TEXT.__const: 0xf4
-  __TEXT.__cstring: 0x22b9
-  __TEXT.__gcc_except_tab: 0xac0
-  __TEXT.__oslogstring: 0x2f32
+  __TEXT.__cstring: 0x22c8
+  __TEXT.__gcc_except_tab: 0xac4
+  __TEXT.__oslogstring: 0x2fb1
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__unwind_info: 0xd90
   __TEXT.__objc_classname: 0x544
-  __TEXT.__objc_methname: 0x877d
+  __TEXT.__objc_methname: 0x87a3
   __TEXT.__objc_methtype: 0x1577
   __TEXT.__objc_stubs: 0x55e0
   __DATA_CONST.__got: 0x240

   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4ff0
-  __DATA_CONST.__objc_selrefs: 0x1b30
+  __DATA_CONST.__objc_selrefs: 0x1b38
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x100
   __AUTH_CONST.__cfstring: 0x1860
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x6c8
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x220
-  __DATA.__objc_superrefs: 0x100
   __DATA.__objc_ivar: 0x37c
   __DATA.__data: 0x52c
   __DATA.__bss: 0xe8
   __DATA.__common: 0x1
-  __DATA_DIRTY.__const: 0x320
+  __DATA_DIRTY.__const: 0x2c0
   __DATA_DIRTY.__objc_const: 0x1280
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__data: 0x40

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 43E7ADB9-2FC3-34E8-92FF-E2261CDB4820
-  Functions: 1370
-  Symbols:   4722
-  CStrings:  2277
+  UUID: 2BD60FC5-DDCA-3170-BF0E-5057249B44B3
+  Functions: 1372
+  Symbols:   4726
+  CStrings:  2281
 
Symbols:
+ -[NSURL(_QLUtilities) _QLIsThumbnailable]
+ -[NSURL(_QLUtilities) _QLIsThumbnailable].cold.1
+ ___71-[QLExternalThumbnailCacheDatabase _createDatabaseIfNeededAtURL:error:]_block_invoke.78
+ ___block_descriptor_49_e8_32s40s_e112_v76?0"NSData"8"QLURLHandler"16"IOSurface"24{CGSize=dd}32"QLTBitmapFormat"48"NSDictionary"56B64"NSError"68ls32l8s40l8
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.118
+ ___block_literal_global.125
+ ___block_literal_global.131
- ___71-[QLExternalThumbnailCacheDatabase _createDatabaseIfNeededAtURL:error:]_block_invoke.77
- ___block_descriptor_40_e8_32s_e112_v76?0"NSData"8"QLURLHandler"16"IOSurface"24{CGSize=dd}32"QLTBitmapFormat"48"NSDictionary"56B64"NSError"68ls32l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.117
- ___block_literal_global.124
- ___block_literal_global.130
CStrings:
+ "<%@:%p maximumSize=(%.2f, %.2f) minimumSize=(%.2f,%.2f) scale=%.1f url=%@ contentType=%@>"
+ "T@\"NSString\",?,R,C"
+ "_QLIsThumbnailable"
+ "stat for %@ failed with errno %{darwin.errno}d; returning YES for _QLIsThumbnailable"
+ "stat for %@ succeeded; thumbnailable = %d"
- "<%@:%p maximumSize=(%.2f, %.2f) minimumSize=(%.2f,%.2f) scale=%.1f url=%@>"

```
