## CloudKit

> `/System/Library/Frameworks/CloudKit.framework/CloudKit`

```diff

-2150.34.1.0.0
-  __TEXT.__text: 0x24a6a0
-  __TEXT.__auth_stubs: 0x31d0
-  __TEXT.__objc_methlist: 0x1b204
+2160.17.1.0.0
+  __TEXT.__text: 0x24ae40
+  __TEXT.__auth_stubs: 0x31e0
+  __TEXT.__objc_methlist: 0x1b25c
   __TEXT.__const: 0x3240
-  __TEXT.__cstring: 0x1ced0
+  __TEXT.__cstring: 0x1cf6d
   __TEXT.__constg_swiftt: 0xe84
   __TEXT.__swift5_typeref: 0x3c30
   __TEXT.__swift5_reflstr: 0x9d2

   __TEXT.__swift5_capture: 0x136c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__gcc_except_tab: 0x9770
-  __TEXT.__oslogstring: 0x139a5
+  __TEXT.__gcc_except_tab: 0x97d8
+  __TEXT.__oslogstring: 0x13a50
   __TEXT.__dlopen_cstrs: 0x136
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0xbfc4
+  __TEXT.__unwind_info: 0xc1ac
   __TEXT.__eh_frame: 0x4c08
   __TEXT.__objc_classname: 0x3961
-  __TEXT.__objc_methname: 0x3bb62
-  __TEXT.__objc_methtype: 0x6d84
+  __TEXT.__objc_methname: 0x3bb8c
+  __TEXT.__objc_methtype: 0x6d72
   __TEXT.__objc_stubs: 0x1fee0
   __DATA_CONST.__got: 0x618
-  __DATA_CONST.__const: 0x6ec8
+  __DATA_CONST.__const: 0x6ef8
   __DATA_CONST.__objc_classlist: 0xd30
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x26f70
-  __DATA_CONST.__objc_selrefs: 0xac00
+  __DATA_CONST.__objc_const: 0x26fb8
+  __DATA_CONST.__objc_selrefs: 0xac28
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_classrefs: 0xe10
   __DATA_CONST.__objc_superrefs: 0xc90

   __AUTH_CONST.__objc_const: 0xbf40
   __AUTH_CONST.__const: 0x8df0
   __AUTH_CONST.__auth_ptr: 0x138
-  __AUTH_CONST.__cfstring: 0x1ae40
+  __AUTH_CONST.__cfstring: 0x1aea0
   __AUTH_CONST.__objc_arrayobj: 0x3d8
-  __AUTH_CONST.__objc_intobj: 0x8a0
+  __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__auth_got: 0x1908
   __AUTH.__objc_data: 0x3cf8
-  __AUTH.__data: 0x528
+  __AUTH.__data: 0x538
   __DATA.__objc_ivar: 0x164c
-  __DATA.__data: 0x48b8
+  __DATA.__data: 0x5158
   __DATA.__common: 0x798
-  __DATA.__bss: 0x4678
+  __DATA.__bss: 0x3e00
   __DATA_DIRTY.__objc_ivar: 0xb78
   __DATA_DIRTY.__objc_data: 0x49c0
   __DATA_DIRTY.__data: 0xf8
   __DATA_DIRTY.__common: 0xb1
-  __DATA_DIRTY.__bss: 0x778
+  __DATA_DIRTY.__bss: 0x740
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15837
-  Symbols:   3856
-  CStrings:  15683
+  Functions: 15851
+  Symbols:   3859
+  CStrings:  15692
 
Symbols:
+ _ACAccountDataclassPhoneFaceTime
+ _CKAddResponseHeaderValuesToUserInfoDictionary
+ _notify_get_state
CStrings:
+ "\x0f\x03"
+ "AccountInfoValidationCounterReset"
+ "Failed to retrieve validation counter with token %d: status %u"
+ "Fetching full account info for CKContainerImplementation %p, containerID %@ on queue %@. Container options: %@"
+ "Invalid or out of range Retry-After header value: %@. Used %d"
+ "Setting the in-memory account info validation counter to %ld for uid %u"
+ "TQ,N,V_flags"
+ "Thu Apr 18 18:50:56 2024"
+ "Tried to end a signpost, but none was in effect"
+ "accountInfoFetchQueue"
+ "bypassPCS"
+ "com.apple.FTMessageStoreService"
+ "com.apple.callhistory.cloud-storage2"
+ "com.apple.cloudkit.accountInfoFetchQueue.bypassesPCS"
+ "com.apple.cloudkit.accountInfoFetchQueue.usesPCS"
+ "isServerJSONThrottle"
+ "isServerProtobufThrottle"
+ "setFlag:"
+ "setFlags:"
+ "setValidAccountInfoValidationCounterValue:"
+ "validAccountInfoValidationCounterValue"
- "\x0f\x04"
- "@40@0:8@16Q24^@32"
- "Fetching full account info for CKContainerImplementation %p, containerID %@"
- "Mon Feb 12 16:33:59 2024"
- "T@\"NSNumber\",&,N,V_isServerThrottle"
- "Tried to and a signpost, but none was in effect"
- "Warn: invalid value (%{public}@) for %{public}@ header field"
- "_isServerThrottle"
- "com.apple.cloudkit.accountInfoFetchQueue"
- "dictionaryWithObjectsAndKeys:"
- "managerForRegistryDatabase:options:error:"
- "setIsServerThrottle:"

```
