## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1402.200.75.2.1
-  __TEXT.__text: 0x1bc658
-  __TEXT.__auth_stubs: 0x2600
+1402.200.111.2.8
+  __TEXT.__text: 0x1bd7e8
+  __TEXT.__auth_stubs: 0x2700
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x13170
+  __TEXT.__objc_methlist: 0x13230
   __TEXT.__const: 0x16b0
-  __TEXT.__gcc_except_tab: 0x15e54
-  __TEXT.__cstring: 0x10557
-  __TEXT.__oslogstring: 0x1df29
+  __TEXT.__gcc_except_tab: 0x15e58
+  __TEXT.__cstring: 0x105d7
+  __TEXT.__oslogstring: 0x1e059
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__constg_swiftt: 0x550

   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x6c
   __TEXT.__swift5_capture: 0x4ac
-  __TEXT.__unwind_info: 0x7cc8
+  __TEXT.__unwind_info: 0x7d10
   __TEXT.__eh_frame: 0x8c8
-  __TEXT.__objc_classname: 0x24c3
-  __TEXT.__objc_methname: 0x3c83e
-  __TEXT.__objc_methtype: 0x647c
-  __TEXT.__objc_stubs: 0x24220
-  __DATA_CONST.__got: 0x1e60
-  __DATA_CONST.__const: 0x4ff0
-  __DATA_CONST.__objc_classlist: 0x718
+  __TEXT.__objc_classname: 0x24dc
+  __TEXT.__objc_methname: 0x3ca81
+  __TEXT.__objc_methtype: 0x6482
+  __TEXT.__objc_stubs: 0x24400
+  __DATA_CONST.__got: 0x1eb8
+  __DATA_CONST.__const: 0x5048
+  __DATA_CONST.__objc_classlist: 0x720
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc7b0
+  __DATA_CONST.__objc_selrefs: 0xc810
   __DATA_CONST.__objc_protorefs: 0x190
-  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x1320
+  __AUTH_CONST.__auth_got: 0x13a0
   __AUTH_CONST.__auth_ptr: 0x318
-  __AUTH_CONST.__const: 0x41a8
-  __AUTH_CONST.__cfstring: 0xbc20
-  __AUTH_CONST.__objc_const: 0x20d20
+  __AUTH_CONST.__const: 0x41c8
+  __AUTH_CONST.__cfstring: 0xbca0
+  __AUTH_CONST.__objc_const: 0x20e60
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x28a0
+  __AUTH.__objc_data: 0x28f0
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x110c
+  __DATA.__objc_ivar: 0x1118
   __DATA.__data: 0x28c0
-  __DATA.__bss: 0x2d38
+  __DATA.__bss: 0x2d48
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x2348
   __DATA_DIRTY.__data: 0x3c8

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8823
-  Symbols:   2309
-  CStrings:  14264
+  Functions: 8853
+  Symbols:   2341
+  CStrings:  14297
 
Symbols:
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CFDataCreate
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDictionaryAddValue
+ _CFStringAppendFormat
+ _CFStringCreateMutable
+ _CFStringGetBytes
+ _CFStringGetCStringPtr
+ _IAChannelMessages
+ _IASignalMessageSent
+ _IMEncryptedIdentifier
+ _IMSharedHelperRetrieveSimDetailsFromTelephony
+ _IMTextInputIdentifier
+ _IMTextInputIdentifierPrefix
+ _IMUTTypeIsGIF
+ _OBJC_CLASS_$_IMTextInputCryptographer
+ _OBJC_METACLASS_$_IMTextInputCryptographer
+ _SecItemAdd
+ _SecItemCopyMatching
+ _arc4random_buf
+ _kCFBooleanTrue
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleWhenUnlocked
+ _kSecAttrApplicationLabel
+ _kSecClass
+ _kSecClassKey
+ _kSecReturnData
+ _kSecValueData
+ _strlen
- _OBJC_CLASS_$_IAUtility
CStrings:
+ "\x0f\x0f\x01\x11\x94\x1b"
+ "%!x(MISSING)"
+ "CKTextInputIdentifiersMigrated"
+ "Do not have deviceSalt when creating digest for name."
+ "IMEncryptedIdentifier"
+ "IMTextInputCryptographer"
+ "IM_"
+ "Received _deviceSalt is nil? %!@(MISSING), length? %!l(MISSING)u, with status: %!d(MISSING)"
+ "Something wrong when creating stringDigest: %!@(MISSING) for: %!@(MISSING)"
+ "T@\"NSData\",R,N"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_dispatchQueue"
+ "T@\"NSString\",C,N,V_cachedRecipientDigest"
+ "T@\"NSString\",C,N,V_cachedRecipientName"
+ "_asyncSetChatBotUserActivityForChat:message:"
+ "_cachedRecipientDigest"
+ "_cachedRecipientName"
+ "_deviceSalt"
+ "_dispatchQueue"
+ "_enumerateChatGUIDPermutationsForChatIdentifier:includingInstantMessageStyle:includingGroupStyle:includingRoomStyle:usingBlock:"
+ "_updatePersonCentricIDForChat:"
+ "businessNameForUID:blockFetch:updateHandler:"
+ "cachedBusinessName"
+ "cachedRecipientDigest"
+ "cachedRecipientName"
+ "com.apple.TextInput"
+ "com.apple.TextInput.crypto"
+ "device salt doesn't exist in the keychain"
+ "deviceSalt"
+ "digest value is empty"
+ "dispatchQueue"
+ "empty input"
+ "failed to add the device salt to the keychain with error: %!d(MISSING)"
+ "failed to create new device salt"
+ "fetchBrandInfoIfNecessary"
+ "isRelayGroupMutationEnabled"
+ "prewarmDeviceSalt"
+ "setCachedRecipientDigest:"
+ "setCachedRecipientName:"
+ "sharedCryptographer"
+ "stringDigestForName:"
+ "v44@0:8@16B24B28B32@?36"
- "\x0f\x0f\x01\x11\x94\x1c"
- "MessageSent"
- "Registering chat %!@(MISSING) using personCentricID %!@(MISSING)"
- "T@\"NSNumber\",&,N,V_chatBot"
- "_chatBot"
- "_enumerateChatGUIDPermutationsForChatIdentifier:styles:usingBlock:"
- "chatBot"
- "getSPIVersion"
- "setChatBot:"
- "v36@0:8@16C24@?28"

```
