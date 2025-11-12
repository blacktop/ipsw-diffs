## installd

> `/usr/libexec/installd`

```diff

-1513.60.10.0.0
-  __TEXT.__text: 0x589e0
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_stubs: 0x7bc0
-  __TEXT.__objc_methlist: 0x3054
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x14eb5
-  __TEXT.__objc_classname: 0x5cd
-  __TEXT.__objc_methname: 0xb374
-  __TEXT.__objc_methtype: 0x1eb4
-  __TEXT.__gcc_except_tab: 0x310c
+1513.60.11.0.0
+  __TEXT.__text: 0x59bc0
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__objc_stubs: 0x7dc0
+  __TEXT.__objc_methlist: 0x315c
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0x1503e
+  __TEXT.__objc_classname: 0x5e3
+  __TEXT.__objc_methname: 0xb6fe
+  __TEXT.__objc_methtype: 0x1f44
+  __TEXT.__gcc_except_tab: 0x3160
   __TEXT.__oslogstring: 0x11ac
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0xfa8
-  __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1088
-  __DATA_CONST.__cfstring: 0x9660
-  __DATA_CONST.__objc_classlist: 0x130
+  __TEXT.__unwind_info: 0xfc0
+  __DATA_CONST.__auth_got: 0x800
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x10b0
+  __DATA_CONST.__cfstring: 0x9740
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_intobj: 0x258
   __DATA_CONST.__objc_arraydata: 0x5d0
   __DATA_CONST.__objc_dictobj: 0xe88
-  __DATA.__objc_const: 0x59c0
-  __DATA.__objc_selrefs: 0x2368
-  __DATA.__objc_ivar: 0x280
-  __DATA.__objc_data: 0xbe0
+  __DATA.__objc_const: 0x5b20
+  __DATA.__objc_selrefs: 0x23f8
+  __DATA.__objc_ivar: 0x290
+  __DATA.__objc_data: 0xc30
   __DATA.__data: 0xa18
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x198
   __DATA.__common: 0x10
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3E50664-061B-320E-9B93-F7EE679320C4
-  Functions: 1202
-  Symbols:   373
-  CStrings:  4677
+  UUID: BA74FF04-E43E-3340-B8AC-B7AD5DADA67E
+  Functions: 1224
+  Symbols:   377
+  CStrings:  4725
 
Symbols:
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMAppInstallation
+ _OBJC_CLASS_$_BMAppInstallationApp
+ _OBJC_CLASS_$_BMAppInstallationMetadata
CStrings:
+ "-[MIInstaller _sendEventToBiomeForIdentity:installedRecord:bundleContainer:installIntent:]"
+ "@\"<MIBiomeSourceProtocol>\""
+ "@\"NSDate\""
+ "App"
+ "Failed to fetch bundle metadata for %@: %@"
+ "Failed to fetch bundle metadata for existing bundle container %@: %@"
+ "Failed to get bundle metadata for %@ within bundleContainer %@: %@"
+ "Installation"
+ "MIBiomeEventManager"
+ "T@\"<MIBiomeSourceProtocol>\",&,N,V_source"
+ "T@\"NSDate\",&,N,V_originalInstallDate"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue"
+ "T@\"NSString\",&,N,V_bundleShortVersion"
+ "T@\"NSString\",&,N,V_bundleVersion"
+ "TB,N,V_isPlaceholderInstall"
+ "TB,N,V_sendToBiome"
+ "_bundleShortVersion"
+ "_bundleVersion"
+ "_originalInstallDate"
+ "_sendEventForIdentity:isPlaceholder:version:shortVersion:originalInstallDate:installSessionID:uniqueInstallID:transition:"
+ "_sendEventToBiomeForIdentity:installedRecord:bundleContainer:installIntent:"
+ "_sendToBiome"
+ "_source"
+ "com.apple.MobileInstallation.MIBiomeEventManager.internal"
+ "initWithApp:transition:metadata:transitionDate:"
+ "initWithBiomeSource:"
+ "initWithBundleID:personaString:isPlaceholder:"
+ "initWithOriginalInstallationDate:version:shortVersion:uniqueInstallID:installSessionID:"
+ "originalInstallDate"
+ "sendEvent:"
+ "sendInstallEventForIdentity:isPlaceholder:version:shortVersion:originalInstallDate:installSessionID:uniqueInstallID:intent:"
+ "sendToBiome"
+ "sendUninstallEventForIdentity:isPlaceholder:version:shortVersion:originalInstallDate:"
+ "setBundleShortVersion:"
+ "setBundleVersion:"
+ "setInternalQueue:"
+ "setIsPlaceholderInstall:"
+ "setOriginalInstallDate:"
+ "setSendToBiome:"
+ "setSource:"
+ "source"
+ "v48@0:8@16@24@32Q40"
+ "v52@0:8@16B24@28@36@44"
+ "v72@0:8@16B24@28@36@44@52@60i68"
+ "v76@0:8@16B24@28@36@44@52@60Q68"
- "T@\"NSString\",R,N,V_updatedBundleShortVersion"
- "T@\"NSString\",R,N,V_updatedBundleVersion"
- "TB,R,N,V_isPlaceholderInstall"
- "_updatedBundleShortVersion"
- "_updatedBundleVersion"
- "setBundleIdentifier:"
- "updatedBundleShortVersion"
- "updatedBundleVersion"

```
