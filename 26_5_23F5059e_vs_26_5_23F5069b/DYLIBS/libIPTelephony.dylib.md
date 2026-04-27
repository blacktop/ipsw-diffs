## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2657.0.0.0.0
-  __TEXT.__text: 0x50e000
+2658.1.0.0.0
+  __TEXT.__text: 0x50e208
   __TEXT.__auth_stubs: 0x2d80
   __TEXT.__init_offsets: 0x158
   __TEXT.__objc_methlist: 0x748
-  __TEXT.__const: 0x2014b
-  __TEXT.__gcc_except_tab: 0x4ecd8
-  __TEXT.__cstring: 0x37b40
-  __TEXT.__oslogstring: 0xfafc
+  __TEXT.__const: 0x2016b
+  __TEXT.__gcc_except_tab: 0x4ecec
+  __TEXT.__cstring: 0x37b7c
+  __TEXT.__oslogstring: 0xfbc6
   __TEXT.__unwind_info: 0x18eb8
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methname: 0x1de8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: FA9D0B2E-CD34-3E85-A7F0-7EE6C19F9D9A
+  UUID: E7A3AEC9-EA6F-3CE2-8B05-F09340C96B29
   Functions: 17054
-  Symbols:   51139
-  CStrings:  10005
+  Symbols:   51140
+  CStrings:  10010
 
Symbols:
+ __ZN9SipHeader14kXRcsGroupInfoE
+ ___block_descriptor_tmp.501
+ ___cxx_global_var_init.396
- ___block_descriptor_tmp.496
- ___cxx_global_var_init.391
Functions:
~ __ZN16SipLazuliManager4sendERK16LazuliSendParamsRK6SipUri : 3668 -> 3720
~ __ZN14MessageSessionC2ENSt3__18weak_ptrI16SipLazuliManagerEERK12ClientConfig : 1464 -> 1460
~ __ZN14MessageSession10initializeENSt3__18weak_ptrI10SDPSessionEENS0_10shared_ptrI9SipDialogEEN3ims14CFMutableArrayERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 3200 -> 3256
~ __ZN14MessageSession15sendMessageBlobERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_S8_jS6_ : 3884 -> 3868
~ __ZN10SipSession28handleInviteOrUpdateResponseENSt3__110shared_ptrIK11SipResponseEENS1_I20SipClientTransactionEE : 10448 -> 11304
~ __ZN14LazuliDelegate18handleSessionReadyENSt3__110shared_ptrIN3ims6lazuli4ChatEEEN3xpc4dictE : 984 -> 1276
~ __ZN14LazuliDelegate22handleGroupChatCreatedENSt3__110shared_ptrIN3ims6lazuli4ChatEEEN3xpc4dictE : 1276 -> 560
CStrings:
+ "#E %{private, mask.hash}sServer detected group fork: %{private}s trx %{private}s encrypted=%{BOOL}d"
+ "%{private, mask.hash}srequesting abc snapshot for group fork with context %s"
+ "%{private, mask.hash}srequesting abc snapshot for registration failure with context %s"
+ "/AppleInternal/Library/BuildRoots/4~COB5ugD7NvCrEvsF5EU0uc5JhXZqqVSfDSBnaWg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/4~COB5ugD7NvCrEvsF5EU0uc5JhXZqqVSfDSBnaWg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "RCSGroupForkEncrypted"
+ "RCSGroupForkPlaintext"
+ "RCSGroupForking"
- "%{private, mask.hash}srequesting abc snapshot with context %s"
- "/AppleInternal/Library/BuildRoots/4~CNX9ugDxophncKPxBY5Eli-Dy4w98Q9ptpOL_tI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~CNX9ugDxophncKPxBY5Eli-Dy4w98Q9ptpOL_tI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"

```
