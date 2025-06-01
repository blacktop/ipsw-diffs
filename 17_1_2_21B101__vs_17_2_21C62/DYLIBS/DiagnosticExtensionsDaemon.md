## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-170.1.0.0.0
-  __TEXT.__text: 0x6d0c8
+170.2.3.0.0
+  __TEXT.__text: 0x6d75c
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x5d2c
+  __TEXT.__objc_methlist: 0x5d54
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x4eff
-  __TEXT.__gcc_except_tab: 0x13d4
-  __TEXT.__oslogstring: 0x807e
+  __TEXT.__cstring: 0x4f69
+  __TEXT.__gcc_except_tab: 0x143c
+  __TEXT.__oslogstring: 0x8345
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x1918
   __TEXT.__objc_classname: 0x871
-  __TEXT.__objc_methname: 0xe85b
+  __TEXT.__objc_methname: 0xe8ed
   __TEXT.__objc_methtype: 0x22e7
-  __TEXT.__objc_stubs: 0xb900
+  __TEXT.__objc_stubs: 0xb9a0
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x1ba0
+  __DATA_CONST.__const: 0x1bc8
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x116d8
-  __DATA_CONST.__objc_selrefs: 0x36c0
+  __DATA_CONST.__objc_const: 0x11718
+  __DATA_CONST.__objc_selrefs: 0x36e8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__cfstring: 0x4a80
+  __AUTH_CONST.__cfstring: 0x4aa0
   __AUTH_CONST.__objc_const: 0x2020
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__const: 0xbc0

   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x500
   __DATA.__objc_superrefs: 0x1a0
-  __DATA.__objc_ivar: 0x598
+  __DATA.__objc_ivar: 0x59c
   __DATA.__data: 0xa40
   __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x8c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5871C5E0-471A-30D9-96DF-31431E5BCDB3
-  Functions: 2714
-  Symbols:   9265
-  CStrings:  5006
+  UUID: 2C430DEF-DE73-30B4-821F-DAF8A9C51BA3
+  Functions: 2719
+  Symbols:   9282
+  CStrings:  5018
 
Symbols:
+ -[DEDBugSession finisherDidCommit]
+ -[DEDBugSession setFinisherDidCommit:]
+ -[DEDDevice publicLogSafeIdentifier]
+ -[DEDIDSInbound local_device_query_callback:service:account:fromID:context:].cold.3
+ _DEDBugSessionDidCommit
+ _OBJC_IVAR_$_DEDBugSession._finisherDidCommit
+ ___56-[DEDBugSession ongoingCollectOperationsWithOperations:]_block_invoke.134
+ ___block_literal_global.136
+ ___block_literal_global.138
+ ___block_literal_global.194
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$finisherDidCommit
+ _objc_msgSend$publicLogSafeIdentifier
+ _objc_msgSend$setFinisherDidCommit:
+ _objc_msgSend$uniqueIDOverride
- ___56-[DEDBugSession ongoingCollectOperationsWithOperations:]_block_invoke.131
- ___block_literal_global.135
- ___block_literal_global.191
CStrings:
+ "\n%s (%@)"
+ "\nDEDDevice: %@ %@ (%@) -- %s"
+ "\x13#\x1f\x03"
+ "Device ready:\nidentifier: %{public}@\nidsIdentifier: %{public}@\naddress: %{private}@\nmodel: %{public}@\nname: %{private}@\nplatform: %{public}@\nbuild: %{public}@\nremoteTransport: %{public}s\ntransport: %{public}s\nstatus: %{public}s\ndeviceClass: %{public}@\nproductType: %{public}@\ncolor: %{public}@\nenclosureColor: %{public}@\nhomeButtonType: %li\nisHomeKitResident: %d\nmediaSystemRole: %li\ncapabilities: %{public}@\n"
+ "Did add device [%i-%{public}@]"
+ "Did clear notification on filing device and finisher has already completed. Will not call finisher again"
+ "Not adding temp device [%i-%{public}@], already have [%{public}@]"
+ "Ping sent: device name: %{private}@ targetID: %{private}@ | [%{public}@]"
+ "RealityDevice"
+ "TB,V_finisherDidCommit"
+ "Will try to add device:\n%{private}@ - %{public}@ %{public}@ (%{public}@) -- %{public}s \n%{public}s (%{public}@) \n%{public}s Remote: (%{private}@ - %{public}@)"
+ "[%{public}s didCommit? %i"
+ "_finisherDidCommit"
+ "containsValueForKey:"
+ "device for incoming device %{public}@ -> %{public}@"
+ "discovered [%i-%{public}@]"
+ "discovered devices [%lu]"
+ "finisherDidCommit"
+ "found temp device [%{public}@] for key [%{private}@]"
+ "https://appleid.cdn-apple.com/static/deviceImages-12.0/RealityDevice/%@/online-sourcelist%@.png"
+ "https://radar-webservices-ext.apple.com"
+ "local_device_query_callback: IDS device ready [%{public}@] on service [%{public}@]"
+ "publicLogSafeIdentifier"
+ "setFinisherDidCommit:"
+ "uniqueIDOverride"
+ "\x91"
- "\x03#\x1f\x03"
- "\n  %s (%@)"
- "\n  Remote: %s (%@)"
- "\n%@ - %@ %@ (%@) -- %s"
- "DEDDevice:"
- "IDS device [%{public}@] responded on service [%{public}@]"
- "IDS device ready: [%{public}@]"
- "Not adding temp device [%{public}@], already have [%{public}@]"
- "Ping sent: device name: %{public}@ targetID: %{public}@"
- "device for incoming device %@ -> %@"
- "did add device [%{public}@]"
- "discovered devices [%lu]: [%{public}@]"
- "found temp device [%{public}@] for key [%{public}@]"
- "https://radar-api.apple.com"
- "will try to add device [%{public}@]"
- "\x81"

```
