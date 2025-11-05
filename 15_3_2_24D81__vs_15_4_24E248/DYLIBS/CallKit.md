## CallKit

> `/System/Library/Frameworks/CallKit.framework/Versions/A/CallKit`

```diff

-1325.400.141.0.0
-  __TEXT.__text: 0x6d698
+1325.500.161.0.0
+  __TEXT.__text: 0x6c384
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x7b0c
+  __TEXT.__objc_methlist: 0x8a34
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x5e38
+  __TEXT.__cstring: 0x5e66
   __TEXT.__oslogstring: 0x33e8
   __TEXT.__gcc_except_tab: 0x6e0
-  __TEXT.__unwind_info: 0x1d10
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__objc_classname: 0x13f6
-  __TEXT.__objc_methname: 0x10cf0
+  __TEXT.__objc_methname: 0x10d89
   __TEXT.__objc_methtype: 0x3b72
-  __TEXT.__objc_stubs: 0xa100
+  __TEXT.__objc_stubs: 0xa160
   __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3038
+  __DATA_CONST.__objc_selrefs: 0x31a0
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x1100
-  __AUTH_CONST.__cfstring: 0x3c80
-  __AUTH_CONST.__objc_const: 0xfb78
+  __AUTH_CONST.__cfstring: 0x3cc0
+  __AUTH_CONST.__objc_const: 0xe0c8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0x884
+  __DATA.__objc_ivar: 0x888
   __DATA.__data: 0x1740
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F0B9ACB0-BC03-3820-85DC-979A406E7428
-  Functions: 3057
-  Symbols:   6779
-  CStrings:  4425
+  UUID: 63670891-DABA-311A-8E9F-D9630FA3A536
+  Functions: 3074
+  Symbols:   6802
+  CStrings:  4435
 
Symbols:
+ +[CXCallDirectoryExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[CXCallDirectoryExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[CXCallDirectoryExtensionHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[CXCallDirectoryExtensionHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[CXCallObserverXPCClient sharedXPCClientSemaphore].cold.1
+ +[CXProviderExtensionContext _extensionAuxiliaryHostProtocol].cold.1
+ +[CXProviderExtensionContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[CXServiceDomain callKitServiceDomain].cold.1
+ +[CXVoicemailObserverXPCClient sharedXPCClientSemaphore].cold.1
+ +[NSString cx_stringWithCXActionOriginator:]
+ -[CXHandle description].cold.1
+ -[CXSetMutedCallAction initWithCallUUID:muted:systemInitiated:]
+ -[CXSetMutedCallAction isSystemInitiated]
+ -[CXSetMutedCallAction setSystemInitiated:]
+ -[CXTransaction allowedClassesForMutableActions].cold.1
+ CXDefaultLog.cold.1
+ CXOversizedLog.cold.1
+ CXOversizedLogQueue.cold.1
+ OBJC_IVAR_$_CXSetMutedCallAction._systemInitiated
+ _objc_msgSend$isSystemInitiated
+ _objc_msgSend$setBottomUpMute:
+ _objc_msgSend$setSystemInitiated:
CStrings:
+ " systemInitiated=%d"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CallKit/CallKit/CXCallDirectoryLabeledPhoneNumberEntryData.m"
+ "CXActionOriginatorUnknown"
+ "TB,N,GisSystemInitiated,V_systemInitiated"
+ "_systemInitiated"
+ "initWithCallUUID:muted:systemInitiated:"
+ "isSystemInitiated"
+ "setSystemInitiated:"
+ "systemInitiated"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CallKit/CallKit/CXCallDirectoryLabeledPhoneNumberEntryData.m"

```
