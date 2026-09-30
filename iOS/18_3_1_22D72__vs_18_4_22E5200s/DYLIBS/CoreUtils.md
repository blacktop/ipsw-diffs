## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-760.36.2.0.0
-  __TEXT.__text: 0x114a3c
-  __TEXT.__auth_stubs: 0x2eb0
-  __TEXT.__objc_methlist: 0x8340
-  __TEXT.__const: 0x2150
-  __TEXT.__gcc_except_tab: 0x1b18
-  __TEXT.__cstring: 0x233ee
-  __TEXT.__oslogstring: 0x3c2
-  __TEXT.__unwind_info: 0x3988
+770.21.0.0.0
+  __TEXT.__text: 0x114d8c
+  __TEXT.__auth_stubs: 0x2f10
+  __TEXT.__objc_methlist: 0x9648
+  __TEXT.__cstring: 0x2338e
+  __TEXT.__const: 0x22d8
+  __TEXT.__gcc_except_tab: 0x1b40
+  __TEXT.__oslogstring: 0x422
+  __TEXT.__unwind_info: 0x3890
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0xbeb
-  __TEXT.__objc_methname: 0x14c1e
-  __TEXT.__objc_methtype: 0x4005
-  __TEXT.__objc_stubs: 0x9d60
-  __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x2990
-  __DATA_CONST.__objc_classlist: 0x300
+  __TEXT.__objc_classname: 0xbbd
+  __TEXT.__objc_methname: 0x14c2b
+  __TEXT.__objc_methtype: 0x40b6
+  __TEXT.__objc_stubs: 0x9e00
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__const: 0x2978
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x148
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4100
+  __DATA_CONST.__objc_selrefs: 0x49a0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x208
-  __AUTH_CONST.__auth_got: 0x1768
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1f50
-  __AUTH_CONST.__cfstring: 0x42c0
-  __AUTH_CONST.__objc_const: 0x15600
+  __DATA_CONST.__objc_superrefs: 0x200
+  __AUTH_CONST.__auth_got: 0x1798
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x1f30
+  __AUTH_CONST.__cfstring: 0x4380
+  __AUTH_CONST.__objc_const: 0x12e28
   __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH.__objc_data: 0x1b80
-  __AUTH.__data: 0xb20
-  __DATA.__objc_ivar: 0x14d0
-  __DATA.__data: 0x3370
-  __DATA.__bss: 0x10b8
+  __AUTH.__objc_data: 0x1b30
+  __AUTH.__data: 0xb00
+  __DATA.__objc_ivar: 0x14b4
+  __DATA.__data: 0x3240
+  __DATA.__bss: 0x10a8
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x178
-  __DATA_DIRTY.__bss: 0x221
+  __DATA_DIRTY.__bss: 0x211
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5706
-  Symbols:   6730
-  CStrings:  9468
+  Functions: 5611
+  Symbols:   6731
+  CStrings:  9453
 
Symbols:
+ _AES_CBCFrame_Update2
+ _AES_ECB_Final
+ _AES_ECB_Init
+ _AES_ECB_Update
+ _Base64DecodedSize
+ _Base64EncodeLinesEx
+ _Base64EncodedLinesMaxSize
+ _CFPreferencesCopyValue
+ _CUEnterSandbox
+ _CUNumericSuffixRemoved
+ _DMAPContentBlock_AddCodeInfo
+ _DMAPContentBlock_AddInt16
+ _DMAPContentBlock_AddUTF8
+ _DataBuffer_AppendAppleGeneralIE
+ _DataBuffer_AppendVendorIE
+ _HTTPMessageSetClientMessageType
+ _IECopyCoalescedVendorSpecific
+ _IPCAgent_Create
+ _IPCAgent_DeleteSync
+ _IPCAgent_Perform
+ _IPCAgent_SetMessageHandler
+ _IPCAgent_Start
+ _OBJC_CLASS_$_NSRegularExpression
+ _SDPFindMediaSectionEx
+ _SDPScanFAttribute
+ __os_log_error_impl
+ __set_user_dir_suffix
+ _cchkdf
+ _ccsha256_di
+ _chacha20_init_96x32
+ _confstr
+ _kCFPreferencesAnyApplication
+ _objc_storeWeak
- _OBJC_CLASS_$_CULiveAction
- _OBJC_METACLASS_$_CULiveAction
- _fmod
CStrings:
+ "\x01H\x12"
+ "\x02\x13Q\x11\x11!\x141\x11\x11\x12\x81\x11!\x14\x11\x121'\"\x12"
+ "### _set_user_dir_suffix failed: %{darwin.errno}d"
+ "### confstr temp dir failed: %{darwin.errno}d"
+ "(.*)\\s+\\(\\d+\\)$"
+ "-[CUSystemMonitorImp _meDeviceOverride]"
+ "@\"<WiFiAwareDataSessionPairingDelegate>\""
+ "FakeFMF"
+ "MeDevice override: IDS %@"
+ "Nora"
+ "Request written: CID 0x%08X, Header %zu bytes, Body %zu bytes%?{end}, Type %'s\n"
+ "Scheduling speaking '%@', flags=%@, volume=%f"
+ "Skipping duplicate connection: %##a"
+ "T@\"<WiFiAwareDataSessionPairingDelegate>\",W,N,V_wfaPairingDelegate"
+ "This Device"
+ "_meDeviceOverride"
+ "_wfaPairingDelegate"
+ "currentAudioAndVideoCallCount"
+ "firstMatchInString:options:range:"
+ "home:didUpdateActionSet:isExecuting:"
+ "initWithPattern:options:error:"
+ "numberOfRanges"
+ "publisher:detectedMulticastError:fromMulticastReceiver:"
+ "publisher:receivedDataBlobForMulticastSession:fromPeer:"
+ "rangeAtIndex:"
+ "setPairingDelegate:"
+ "setPrivacySensitive:"
+ "setWfaPairingDelegate:"
+ "subscriber:detectedMulticastError:fromMulticastSender:"
+ "subscriber:receivedDataBlobForMulticastSession:fromPeer:"
+ "substringWithRange:"
+ "v36@0:8@\"HMHome\"16@\"HMActionSet\"24B32"
+ "v40@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwarePublisher\"16q24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwareSubscriber\"16@\"NSData\"24@\"WiFiMACAddress\"32"
+ "v40@0:8@\"WiFiAwareSubscriber\"16q24@\"WiFiMACAddress\"32"
+ "wfaPairingDelegate"
+ "\xd1"
- "\x01J"
- "\x02\x14Q\x11\x11!\x14!\x11\x11\x12\x81\x11!\x14\x11\x121'\"\x12"
- "-1"
- "-[CULiveAction activateWithCompletion:]_block_invoke"
- "-[CULiveAction invalidate]_block_invoke"
- "-[CUSystemMonitorImp callObserver:callChanged:]"
- ".."
- "/System/Library/Frameworks/CallKit.framework/CallKit"
- "@\"CXCallObserver\""
- "@32@0:8@\"NSObject<OS_xpc_object>\"16^@24"
- "CF"
- "CULiveAction"
- "CUXPCCodable"
- "CXCallObserver"
- "CXCallObserverDelegate"
- "CallKit changed\n"
- "Not supported, use HomeKit instead"
- "Request written: CID 0x%08X, Header %zu bytes, Body %zu bytes\n"
- "Scheduling speaking '%@'\n"
- "T@\"NSArray\",C,N,V_destinationIDs"
- "T@\"NSString\",C,N,V_originatingHomeKitAccessoryID"
- "T@\"NSString\",C,N,V_speakText"
- "T@\"NSURL\",C,N,V_soundFileURL"
- "TB,N,V_direct"
- "Ti,N,V_alertType"
- "XPC non-dict"
- "_alertType"
- "_callObserver"
- "_destinationIDs"
- "_direct"
- "_originatingHomeKitAccessoryID"
- "_soundFileURL"
- "_speakText"
- "alertType"
- "callObserver:callChanged:"
- "calls"
- "destinationIDs"
- "direct"
- "hasConnected"
- "hasEnded"
- "originatingHomeKitAccessoryID"
- "setAlertType:"
- "setDelegate:queue:"
- "setDestinationIDs:"
- "setDirect:"
- "setOriginatingHomeKitAccessoryID:"
- "setSoundFileURL:"
- "setSpeakText:"
- "soundFileURL"
- "speakText"
- "user:didUpdatePersonManagerSettings:"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v32@0:8@\"CXCallObserver\"16@\"CXCall\"24"

```
