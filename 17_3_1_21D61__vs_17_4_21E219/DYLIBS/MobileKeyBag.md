## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-621.40.2.0.0
-  __TEXT.__text: 0x1b5a0
-  __TEXT.__auth_stubs: 0x1370
+625.100.7.0.0
+  __TEXT.__text: 0x1ba04
+  __TEXT.__auth_stubs: 0x1390
   __TEXT.__objc_methlist: 0x260
-  __TEXT.__cstring: 0x7a3f
+  __TEXT.__cstring: 0x7aa7
   __TEXT.__const: 0x4e6
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x620
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__unwind_info: 0x860
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x145f
-  __TEXT.__objc_methtype: 0x99f
-  __TEXT.__objc_stubs: 0x1020
+  __TEXT.__objc_methname: 0x14e9
+  __TEXT.__objc_methtype: 0x9b0
+  __TEXT.__objc_stubs: 0x10a0
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x738
+  __DATA_CONST.__const: 0x778
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xca0
-  __DATA_CONST.__objc_selrefs: 0x430
-  __AUTH_CONST.__cfstring: 0x4ea0
-  __AUTH_CONST.__const: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__cfstring: 0x4dc0
+  __AUTH_CONST.__const: 0x680
   __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x9c8
+  __AUTH_CONST.__auth_got: 0x9d8
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x30
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x378
+  __DATA.__data: 0x368
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 529
-  Symbols:   1698
-  CStrings:  1268
+  Functions: 536
+  Symbols:   1719
+  CStrings:  1282
 
Symbols:
+ -[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]
+ -[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]
+ _MKBBackupCopyKeyWithError
+ _MKBBackupUpdateKeyWithError
+ _MKBUnlockDeviceForACMRef
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSNumber
+ _ObjectOrNull
+ ___65-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke
+ ___65-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke_2
+ ___68-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]_block_invoke
+ ___68-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]_block_invoke_2
+ ___MKBUnlockDeviceForACMRef_block_invoke
+ ___analytics_send_db_add_block_invoke
+ ___analytics_send_db_get_block_invoke
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.150
+ ___block_descriptor_tmp.54
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.85
+ ___block_descriptor_tmp.87
+ ___block_descriptor_tmp.96
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.226
+ ___block_literal_global.228
+ ___block_literal_global.230
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.236
+ ___block_literal_global.239
+ ___block_literal_global.242
+ ___block_literal_global.244
+ ___block_literal_global.246
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.263
+ ___block_literal_global.268
+ ___block_literal_global.273
+ ___block_literal_global.278
+ ___block_literal_global.280
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.286
+ ___block_literal_global.288
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.294
+ ___block_literal_global.296
+ ___block_literal_global.298
+ _analytics_send_db_add
+ _analytics_send_db_get
+ _objc_autorelease
+ _objc_msgSend$SeshatUnlock:withMemento:verifyOnly:withACMRef:
+ _objc_msgSend$SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$getBackupkeyForVolume:andCryptoID:withError:
+ _objc_msgSend$null
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_retain
+ _objc_retain_x19
- -[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:]
- -[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withreturnValue:]
- ___57-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:]_block_invoke
- ___57-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:]_block_invoke_2
- ___71-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withreturnValue:]_block_invoke
- ___71-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withreturnValue:]_block_invoke_2
- ___MKBUnlockDevice_block_invoke
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.152
- ___block_descriptor_tmp.157
- ___block_descriptor_tmp.166
- ___block_descriptor_tmp.178
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.88
- ___block_descriptor_tmp.98
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.208
- ___block_literal_global.210
- ___block_literal_global.212
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.238
- ___block_literal_global.241
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.255
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.267
- ___block_literal_global.269
- ___block_literal_global.272
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.297
- ___isInternalBuild_block_invoke
- ___stderrp
- _fprintf
- _isInternalBuild.bIsInternal
- _isInternalBuild.onceToken
- _objc_msgSend$SeshatUnlock:withMemento:verifyOnly:
- _objc_msgSend$SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withReply:
- _objc_msgSend$getBackupkeyForVolume:andCryptoID:withreturnValue:
CStrings:
+ "-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]"
+ "-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:withACMRef:]_block_invoke"
+ "-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke"
+ "-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withError:]_block_invoke_2"
+ "@40@0:8@16Q24^@32"
+ "AnalyticsEvent: status: %llu"
+ "Could not get the backup key for crypto ID 0x%016qx (%d of %u, existing keys: %s, found1:%d, found2:%d, found3:%d)"
+ "Error: %@"
+ "MKBUnlockDeviceForACMRef"
+ "MobileKeyBagError"
+ "SeshatUnlock:withMemento:verifyOnly:withACMRef:"
+ "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withACMRef:withReply:"
+ "T@\"NSString\",?,R,C"
+ "analytics_send_db_add"
+ "analytics_send_db_get"
+ "com.apple.mobile.keybagd.db.add"
+ "com.apple.mobile.keybagd.db.get"
+ "cryptoId"
+ "dbError"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "existingKeyError"
+ "fileError"
+ "getBackupkeyForVolume:andCryptoID:withError:"
+ "i40@0:8@16B24B28@32"
+ "null"
+ "numberWithUnsignedLongLong:"
+ "status"
+ "v56@0:8@\"NSFileHandle\"16Q24B32B36@\"NSData\"40@?<v@?i@\"NSError\">48"
+ "v56@0:8@16Q24B32B36@40@?48"
- "-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:]"
- "-[MKBKeyStoreDevice SeshatUnlock:withMemento:verifyOnly:]_block_invoke"
- "-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withreturnValue:]_block_invoke"
- "-[MKBKeyStoreDevice getBackupkeyForVolume:andCryptoID:withreturnValue:]_block_invoke_2"
- "@40@0:8@16Q24^i32"
- "Could not find backup key in backup db, but no error? Return default error..."
- "Could not get the backup key for crypto ID 0x%016qx (%d of %u, existing keys: %s, ret1:%d, ret2:%d, ret3:%d)"
- "Found backup key in backup db, but error %d? Ignore..."
- "MKBUnlockDevice"
- "SeshatUnlock:withMemento:verifyOnly:"
- "SeshatUnlockWithSecret:secretSize:withMemento:verifyOnly:withReply:"
- "getBackupkeyForVolume:andCryptoID:withreturnValue:"
- "i32@0:8@16B24B28"
- "v48@0:8@\"NSFileHandle\"16Q24B32B36@?<v@?i@\"NSError\">40"
- "v48@0:8@16Q24B32B36@?40"

```
