## InstalledContentLibrary

> `/System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary`

```diff

-1270.2.2.0.0
-  __TEXT.__text: 0x92e5c
-  __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x4070
+1270.40.12.0.0
+  __TEXT.__text: 0x92b9c
+  __TEXT.__auth_stubs: 0x1300
+  __TEXT.__objc_methlist: 0x4088
   __TEXT.__const: 0xdf70
-  __TEXT.__gcc_except_tab: 0x920
-  __TEXT.__cstring: 0x14b61
+  __TEXT.__gcc_except_tab: 0x924
+  __TEXT.__cstring: 0x14b92
   __TEXT.__dlopen_cstrs: 0x111
   __TEXT.__oslogstring: 0x8b6
-  __TEXT.__unwind_info: 0x119c
+  __TEXT.__unwind_info: 0x11a0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x55e
-  __TEXT.__objc_methname: 0xc395
-  __TEXT.__objc_methtype: 0x1621
-  __TEXT.__objc_stubs: 0x7a20
+  __TEXT.__objc_methname: 0xc3b7
+  __TEXT.__objc_methtype: 0x1631
+  __TEXT.__objc_stubs: 0x7a40
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__const: 0x1190
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5d40
-  __DATA_CONST.__objc_selrefs: 0x2420
+  __DATA_CONST.__objc_const: 0x5d60
+  __DATA_CONST.__objc_selrefs: 0x2428
   __DATA_CONST.__objc_arraydata: 0x9a0
-  __AUTH_CONST.__cfstring: 0xb8e0
+  __AUTH_CONST.__cfstring: 0xb920
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__const: 0x4a50
   __AUTH_CONST.__objc_dictobj: 0x11a8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH_CONST.__auth_got: 0x990
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x268
   __DATA.__objc_superrefs: 0x150

   __DATA_DIRTY.__objc_const: 0x1c88
   __DATA_DIRTY.__objc_data: 0x1180
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1d0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA8A1A5D-55B8-3CC4-83EE-6CE67007A3FD
-  Functions: 1720
+  UUID: A4B12F17-723B-3121-8B41-7767F01E76B8
+  Functions: 1721
   Symbols:   6002
-  CStrings:  5515
+  CStrings:  5520
 
Symbols:
+ -[MIBundle currentOSVersionForValidationUsingPlatform:withError:]
+ -[MIBundle isDeletable]
+ -[MIDriverKitBundle currentOSVersionForValidationUsingPlatform:withError:]
+ -[MIEmbeddedWatchBundle currentOSVersionForValidationUsingPlatform:withError:]
+ -[MIGlobalConfiguration hasEAPFSVolumeSplit]
+ -[MIPluginKitBundle currentOSVersionForValidationUsingPlatform:withError:]
+ GCC_except_table55
+ GCC_except_table61
+ _objc_msgSend$currentOSVersionForValidationUsingPlatform:withError:
+ _objc_msgSend$hasEAPFSVolumeSplit
- -[MIBundle currentOSVersionForValidationWithError:]
- -[MIDriverKitBundle currentOSVersionForValidationWithError:]
- -[MIEmbeddedWatchBundle currentOSVersionForValidationWithError:]
- -[MIPluginKitBundle currentOSVersionForValidationWithError:]
- GCC_except_table27
- GCC_except_table51
- GCC_except_table56
- _MISProvisioningProfileGetEntitlements
- _MISProvisioningProfileIsForLocalProvisioning
- ___42-[MIDaemonConfiguration deviceHasPersonas]_block_invoke
- _deviceHasPersonas.readOnceToken
- _objc_msgSend$currentOSVersionForValidationWithError:
CStrings:
+ "-[MIBundle currentOSVersionForValidationUsingPlatform:withError:]"
+ "-[MIDriverKitBundle currentOSVersionForValidationUsingPlatform:withError:]"
+ "/private/var/PersonaVolumes/"
+ "/var/PersonaVolumes/"
+ "@32@0:8^Q16^@24"
+ "Forcing system staging root for persona volume path %@"
+ "currentOSVersionForValidationUsingPlatform:withError:"
+ "hasEAPFSVolumeSplit"
- "-[MIBundle currentOSVersionForValidationWithError:]"
- "-[MIDriverKitBundle currentOSVersionForValidationWithError:]"
- "Profile %@ did not have application-identifier entitlement"
- "_SweepProfilesForProfile"
- "currentOSVersionForValidationWithError:"

```
