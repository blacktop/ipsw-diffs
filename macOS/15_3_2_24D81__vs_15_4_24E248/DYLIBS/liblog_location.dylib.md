## liblog_location.dylib

> `/usr/lib/log/liblog_location.dylib`

```diff

-2956.0.6.0.0
-  __TEXT.__text: 0x54e4
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0x2f0
+2960.0.57.0.0
+  __TEXT.__text: 0x5bf0
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_methlist: 0x32c
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__cstring: 0x343a
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__cstring: 0x3873
+  __TEXT.__unwind_info: 0x150
   __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methname: 0xe99
+  __TEXT.__objc_methname: 0x1004
   __TEXT.__objc_methtype: 0xb4
-  __TEXT.__objc_stubs: 0x600
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x868
+  __TEXT.__objc_stubs: 0x6c0
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x318
+  __DATA_CONST.__objc_selrefs: 0x370
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x50
-  __AUTH_CONST.__cfstring: 0x4140
+  __AUTH_CONST.__cfstring: 0x4600
   __AUTH_CONST.__objc_const: 0xf8
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x810
+  __DATA.__data: 0x820
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57DB2F5F-2CAC-3DD4-A42A-C5C4647B51AC
-  Functions: 78
-  Symbols:   458
-  CStrings:  1160
+  UUID: 6618417C-0F79-3596-A824-6CFAEC977EBA
+  Functions: 83
+  Symbols:   480
+  CStrings:  1248
 
Symbols:
+ -[CLLogFormatter JSONObjectWith_CLClientServiceType:info:]
+ -[CLLogFormatter JSONObjectWith_Encrypted_CLClientLocation:info:]
+ -[CLLogFormatter JSONObjectWith_Encrypted_CLLocationCoordinate2D:info:]
+ -[CLLogFormatter JSONObjectWith_Encrypted_latitude:info:]
+ -[CLLogFormatter JSONObjectWith_Encrypted_longitude:info:]
+ GCC_except_table63
+ GCC_except_table74
+ OSLogCopyFormattedStringImpl.cold.1
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSFileManager
+ __ZL20extractEncryptedDataP11objc_objectPmPP8NSObject
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ _ccaes_ecb_decrypt_mode
+ _ccecb_block_size
+ _ccecb_one_shot
+ _localtime
+ _logObject_Internal_Default
+ _objc_msgSend$currentDirectoryPath
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$stringByAppendingFormat:
+ _onceToken_Internal_Default
+ _snprintf
- GCC_except_table62
- GCC_except_table68
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
CStrings:
+ "/%s"
+ "CLClientManager_Type::AuthorizationRequestTypePinnedLocation"
+ "CLClientServiceType"
+ "JSONObjectWith_CLClientServiceType:info:"
+ "JSONObjectWith_Encrypted_CLClientLocation:info:"
+ "JSONObjectWith_Encrypted_CLLocationCoordinate2D:info:"
+ "JSONObjectWith_Encrypted_latitude:info:"
+ "JSONObjectWith_Encrypted_longitude:info:"
+ "NSData"
+ "can't load key"
+ "currentDirectoryPath"
+ "dataWithBytes:length:"
+ "dataWithContentsOfFile:options:error:"
+ "datatype size mismatch (CLClientLocation)"
+ "datatype size mismatch (CLLocationCoordinate2D)"
+ "datatype size mismatch (double)"
+ "decrypt failure"
+ "decryption failed"
+ "defaultManager"
+ "encrypted data"
+ "expected key"
+ "fileExistsAtPath:"
+ "kCLClientServiceAutoPrompting"
+ "kCLClientServiceBackgroundLaunchable"
+ "kCLClientServiceBackgroundLocation"
+ "kCLClientServiceBackgroundLocationCapable"
+ "kCLClientServiceFullPrecision"
+ "kCLClientServiceLocation"
+ "kCLClientServiceMax"
+ "kCLClientServiceMicroLocation_Deprecated"
+ "kCLClientServiceNonPersistentSLC"
+ "kCLClientServiceOnBehalfRegionMonitoring"
+ "kCLClientServicePersistentSLC"
+ "kCLClientServicePush"
+ "kCLClientServiceRanging"
+ "kCLClientServiceReceivingLocationInformation"
+ "kCLClientServiceRegionBeacon"
+ "kCLClientServiceRegionCircular"
+ "kCLClientServiceRemoteLocation_Deprecated"
+ "kCLClientServiceRemoteRegionCircular_Deprecated"
+ "kCLClientServiceSLV"
+ "kCLClientServiceSession"
+ "kCLClientServiceTranscript"
+ "kCLClientServiceUsageIndicatorDiscretion"
+ "keypath"
+ "logkey_%04d_%03d_%02d"
+ "missing key"
+ "reason"
+ "stringByAppendingFormat:"
+ "wrong key (tag mismatch)"

```
