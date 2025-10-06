## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-189.0.0.0.0
-  __TEXT.__text: 0x25b30
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x267c
+198.0.0.0.0
+  __TEXT.__text: 0x2503c
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x261c
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x3fe0
+  __TEXT.__cstring: 0x3e25
   __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__oslogstring: 0x15d3
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__unwind_info: 0x888
   __TEXT.__objc_classname: 0x529
-  __TEXT.__objc_methname: 0x74fa
+  __TEXT.__objc_methname: 0x73b6
   __TEXT.__objc_methtype: 0x1212
-  __TEXT.__objc_stubs: 0x4ac0
+  __TEXT.__objc_stubs: 0x4a20
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xe58
   __DATA_CONST.__objc_classlist: 0x130

   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4328
-  __DATA_CONST.__objc_selrefs: 0x17e0
-  __AUTH_CONST.__cfstring: 0x1ec0
+  __DATA_CONST.__objc_selrefs: 0x1780
+  __AUTH_CONST.__cfstring: 0x1d60
   __AUTH_CONST.__objc_const: 0x1208
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x240

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B9940EA7-869B-3B96-B9D0-60F9C65BBE2A
-  Functions: 1146
-  Symbols:   3894
-  CStrings:  2156
+  UUID: 827A2FD9-4899-3DD3-902F-B16C988EDA63
+  Functions: 1133
+  Symbols:   3857
+  CStrings:  2117
 
Symbols:
+ _NSLog
- +[NSData(RCAdditions) rc_randomDataWithLength:]
- -[NSData(RCAdditions) rc_URLSafeBase64EncodedStringWithOptions:]
- -[NSData(RCAdditions) rc_decryptAESSIVWithKey:additionalData:]
- -[NSData(RCAdditions) rc_decryptAESSIVWithKey:additionalData:].cold.1
- -[NSData(RCAdditions) rc_encryptAESSIVWithKey:additionalData:]
- -[NSData(RCAdditions) rc_encryptAESSIVWithKey:additionalData:].cold.1
- -[NSData(RCAdditions) rc_sha256]
- -[NSData(RCAdditions) rc_zlibDeflate]
- -[NSData(RCAdditions) rc_zlibInflate]
- _CCRandomGenerateBytes
- _CC_SHA256
- _RCGeneralDeviceString
- _RCGeneralDeviceString.cold.1
- __OBJC_$_CLASS_METHODS_NSData(RCAdditions)
- _ccaes_siv_decrypt_mode
- _ccaes_siv_encrypt_mode
- _ccsiv_ciphertext_size
- _ccsiv_one_shot
- _ccsiv_plaintext_size
- _objc_msgSend$base64EncodedStringWithOptions:
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$hasPrefix:
- _objc_msgSend$initWithLength:
- _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
CStrings:
+ "%@"
- ""
- "+"
- "-"
- "-[NSData(RCAdditions) rc_decryptAESSIVWithKey:additionalData:]"
- "-[NSData(RCAdditions) rc_encryptAESSIVWithKey:additionalData:]"
- "/"
- "/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/Categories/NSData+RCAdditions.m"
- "/Library/Caches/com.apple.xbs/Sources/RemoteConfiguration/RemoteConfiguration/RCDeviceInfo.m"
- "="
- "DeviceName"
- "Mac"
- "NSString *RCGeneralDeviceString(void)"
- "_"
- "base64EncodedStringWithOptions:"
- "dataWithBytes:length:"
- "hasPrefix:"
- "iPad"
- "iPhone"
- "iPod"
- "initWithLength:"
- "key != nil"
- "rc_URLSafeBase64EncodedStringWithOptions:"
- "rc_decryptAESSIVWithKey:additionalData:"
- "rc_encryptAESSIVWithKey:additionalData:"
- "rc_randomDataWithLength:"
- "rc_sha256"
- "rc_zlibDeflate"
- "rc_zlibInflate"
- "replaceOccurrencesOfString:withString:options:range:"
- "unrecognized device name"

```
