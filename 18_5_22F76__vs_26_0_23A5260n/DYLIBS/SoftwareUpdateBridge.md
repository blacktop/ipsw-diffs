## SoftwareUpdateBridge

> `/System/Library/PrivateFrameworks/SoftwareUpdateBridge.framework/SoftwareUpdateBridge`

```diff

-350.100.2.0.0
-  __TEXT.__text: 0x6d38
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x820
+364.0.0.0.0
+  __TEXT.__text: 0x72dc
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_methlist: 0x858
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x10d5
-  __TEXT.__oslogstring: 0xa32
-  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__cstring: 0x1168
+  __TEXT.__oslogstring: 0xbe5
+  __TEXT.__unwind_info: 0x1f0
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x1d54
-  __TEXT.__objc_methtype: 0x1fb
+  __TEXT.__objc_methname: 0x1dff
+  __TEXT.__objc_methtype: 0x20f
   __TEXT.__objc_stubs: 0xfe0
-  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xdc0
-  __AUTH_CONST.__objc_const: 0xf38
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0xec0
+  __AUTH_CONST.__objc_const: 0xf98
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__data: 0x290
-  __DATA.__bss: 0x28
-  __DATA.__common: 0x10
+  __DATA.__objc_ivar: 0xc8
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0x48
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9CB780A-3AEF-3CC3-A0D9-CE68E77099EC
-  Functions: 204
-  Symbols:   894
-  CStrings:  701
+  UUID: 419559F2-5A9E-356F-9AE7-3AC21F374B04
+  Functions: 215
+  Symbols:   928
+  CStrings:  733
 
Symbols:
+ -[SUBDescriptor coreDescriptor]
+ -[SUBDescriptor setCoreDescriptor:]
+ -[SUBManager adoptSimulationFileOfName:]
+ -[SUBProgress isStalled]
+ -[SUBProgress setIsStalled:]
+ _CFPreferencesCopyValue
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_SUCoreDescriptor
+ _OBJC_IVAR_$_SUBDescriptor._coreDescriptor
+ _OBJC_IVAR_$_SUBProgress._isStalled
+ _SUBIsRunningInStandaloneGizmoMode
+ _SUBIsRunningInStandaloneGizmoMode.cold.1
+ _SUBIsRunningInStandaloneGizmoMode.onceToken
+ _SUBIsRunningInStandaloneGizmoMode.result
+ _SUBMessageSimulationFileNameKey
+ _SUBMessageTypeSetSimulationFile
+ ___SUBIsRunningInStandaloneGizmoMode_block_invoke
+ ___block_literal_global.299
+ ___block_literal_global.310
+ ___copySUBSimulationFileName_block_invoke
+ _copySUBSimulationFileName
+ _copySUBSimulationFileName.cold.1
+ _copySUBSimulationFileName.onceToken
+ _copySUBSimulationFileName.simulationFileName
+ _kCFPreferencesAnyHost
+ _xpc_connection_send_message_with_reply_sync
- __SUBTransactionCounter
CStrings:
+ "\n            terms: %s userInstallRequestType: %s installTonightScheduled: %s displayTermsRequested: %s\n            ProductVersion: %@\n            ProductBuildVersion: %@\n            ProductSystemName: %@\n            Publisher: %@\n            DownloadSize: %lld\n            PreparationSize: %lld\n            InstallationSize: %lld\n            TotalRequiredFreeSpace: %lld\n            DocumentationID: %@\n            MarketingVersion: %@\n            CurrentDenialReasons: %@\n            OSName: %@\n            Manifest Length: %lu\n             Terms Length: %lu\n            Release Note Length: %lu\n            Release Note Summary Length: %lu \n            SUIconPresent: %@\n             Power Policy: %@\n             CoreDescriptor: %@"
+ "@\"SUCoreDescriptor\""
+ "Found default for simulator file %@"
+ "InternalBuild"
+ "Not present"
+ "Present"
+ "SUCoreDescriptor"
+ "SetSimulationFile"
+ "SimulationFileName"
+ "StandAloneGizmoMode"
+ "T@\"SUCoreDescriptor\",&,N,V_coreDescriptor"
+ "TB,N,V_isStalled"
+ "[AdoptSimulationFile]: Got XPC error while trying to adopt simulation file of name %@"
+ "[AdoptSimulationFile]: Got error while trying to adopt simulation file %@: %@"
+ "[AdoptSimulationFile]: Got unexpected response when trying to adopt simulation file of name %@"
+ "[AdoptSimulationFile]: Parsing response to adopt simulation file(%@) request"
+ "[AdoptSimulationFile]: Successfully adopted simulation file %@"
+ "_coreDescriptor"
+ "_isStalled"
+ "adoptSimulationFileOfName:"
+ "coreDescriptor"
+ "isStalled"
+ "mobile"
+ "setCoreDescriptor:"
+ "setIsStalled:"
- "\n            terms: %s userInstallRequestType: %s installTonightScheduled: %s displayTermsRequested: %s\n            ProductVersion: %@\n            ProductBuildVersion: %@\n            ProductSystemName: %@\n            Publisher: %@\n            DownloadSize: %lld\n            PreparationSize: %lld\n            InstallationSize: %lld\n            TotalRequiredFreeSpace: %lld\n            DocumentationID: %@\n            MarketingVersion: %@\n            CurrentDenialReasons: %@\n            OSName: %@\n            Manifest Length: %lu\n             Terms Length: %lu\n            Release Note Length: %lu\n            Release Note Summary Length: %lu \n            SUIconPresent: %@\n             Power Policy: %@"

```
