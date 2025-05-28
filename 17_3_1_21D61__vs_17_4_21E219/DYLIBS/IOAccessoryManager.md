## IOAccessoryManager

> `/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`

```diff

-958.82.1.0.0
-  __TEXT.__text: 0x24408
+971.102.1.0.0
+  __TEXT.__text: 0x24880
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x2fac
+  __TEXT.__objc_methlist: 0x305c
   __TEXT.__const: 0x818
-  __TEXT.__oslogstring: 0x5359
-  __TEXT.__cstring: 0x4864
+  __TEXT.__oslogstring: 0x5383
+  __TEXT.__cstring: 0x4922
   __TEXT.__ustring: 0x3fc
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__objc_classname: 0x1d4
-  __TEXT.__objc_methname: 0x89d7
+  __TEXT.__objc_methname: 0x8ba5
   __TEXT.__objc_methtype: 0xe71
-  __TEXT.__objc_stubs: 0x4760
+  __TEXT.__objc_stubs: 0x4800
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x66d0
-  __DATA_CONST.__objc_selrefs: 0x1b20
+  __DATA_CONST.__objc_const: 0x67c0
+  __DATA_CONST.__objc_selrefs: 0x1b98
+  __DATA_CONST.__objc_classrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x3040
+  __AUTH_CONST.__cfstring: 0x30a0
   __AUTH_CONST.__objc_const: 0x508
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_classrefs: 0x1a8
-  __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0x77c
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x790
   __DATA.__data: 0x248
   __DATA.__common: 0x58
-  __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x58
+  __DATA.__bss: 0x30
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0x60
   __DATA_DIRTY.__common: 0x140
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1186
-  Symbols:   3921
-  CStrings:  2569
+  Functions: 1202
+  Symbols:   3964
+  CStrings:  2602
 
Symbols:
+ -[IOAccessorySystemStateEndpoint notifyBootComplete]
+ -[IOAccessorySystemStateEndpoint notifyBootComplete].cold.1
+ -[IOAccessorySystemStateMonitor bootComplete]
+ -[IOAccessorySystemStateMonitor bootToken]
+ -[IOAccessorySystemStateMonitor displayEnabled]
+ -[IOAccessorySystemStateMonitor notifyEndpointsBootComplete:]
+ -[IOAccessorySystemStateMonitor pmUserActive]
+ -[IOAccessorySystemStateMonitor processBootState]
+ -[IOAccessorySystemStateMonitor processPMUserActiveState:]
+ -[IOAccessorySystemStateMonitor setBootComplete:]
+ -[IOAccessorySystemStateMonitor setBootToken:]
+ -[IOAccessorySystemStateMonitor setDisplayEnabled:]
+ -[IOAccessorySystemStateMonitor setPmUserActive:]
+ -[IOPortLDCMManagerV4 deviceClass]
+ -[IOPortLDCMManagerV4 setDeviceClass:]
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_IVAR_$_IOAccessorySystemStateMonitor._bootComplete
+ _OBJC_IVAR_$_IOAccessorySystemStateMonitor._bootToken
+ _OBJC_IVAR_$_IOAccessorySystemStateMonitor._displayEnabled
+ _OBJC_IVAR_$_IOAccessorySystemStateMonitor._pmUserActive
+ _OBJC_IVAR_$_IOPortLDCMManagerV4._deviceClass
+ ___37-[IOAccessorySystemStateMonitor init]_block_invoke_5
+ _objc_msgSend$modelSpecificLocalizedStringKeyForKey:
+ _objc_msgSend$notifyBootComplete
+ _objc_msgSend$notifyEndpointsBootComplete:
+ _objc_msgSend$processBootState
+ _objc_msgSend$processPMUserActiveState:
CStrings:
+ "%s boot completed notifying %lu endpoints"
+ "-[IOAccessorySystemStateEndpoint notifyBootComplete]"
+ "-[IOAccessorySystemStateMonitor notifyEndpointsBootComplete:]"
+ "1!"
+ "DeviceClass"
+ "Disconnect cable from charger and device. Unplug charger and allow all connectors to dry. This may take several hours."
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_bootComplete"
+ "TB,N,V_displayEnabled"
+ "TB,N,V_pmUserActive"
+ "Ti,N,V_bootToken"
+ "Ti,N,V_deviceClass"
+ "_bootComplete"
+ "_bootToken"
+ "_deviceClass"
+ "_displayEnabled"
+ "_pmUserActive"
+ "bootComplete"
+ "bootToken"
+ "com.apple.RealitySimulation.DisplayRevealFirstBoot"
+ "deviceClass"
+ "displayEnabled"
+ "iPad"
+ "iPhone"
+ "modelSpecificLocalizedStringKeyForKey:"
+ "notifyBootComplete"
+ "notifyEndpointsBootComplete:"
+ "pmUserActive"
+ "processBootState"
+ "processPMUserActiveState:"
+ "setBootComplete:"
+ "setBootToken:"
+ "setDeviceClass:"
+ "setDisplayEnabled:"
+ "setPmUserActive:"
- "!!"
- "Disconnect cable from charger and iPhone. Unplug charger and allow all connectors to dry. This may take several hours."

```
