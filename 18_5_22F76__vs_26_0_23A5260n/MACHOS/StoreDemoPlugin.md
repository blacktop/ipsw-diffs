## StoreDemoPlugin

> `/System/Library/SpringBoardPlugins/StoreDemoPlugin.servicebundle/StoreDemoPlugin`

```diff

-1445.122.3.0.0
-  __TEXT.__text: 0xb974
+1604.0.0.0.0
+  __TEXT.__text: 0xabac
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x2740
-  __TEXT.__objc_methlist: 0xe2c
-  __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x1b4
-  __TEXT.__oslogstring: 0x12ab
-  __TEXT.__cstring: 0xdaf
-  __TEXT.__objc_classname: 0x17a
-  __TEXT.__objc_methname: 0x2b26
-  __TEXT.__objc_methtype: 0x4a5
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__objc_stubs: 0x2480
+  __TEXT.__objc_methlist: 0xcbc
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__oslogstring: 0x1177
+  __TEXT.__cstring: 0xb19
+  __TEXT.__objc_classname: 0x152
+  __TEXT.__objc_methname: 0x2890
+  __TEXT.__objc_methtype: 0x480
+  __TEXT.__unwind_info: 0x2a8
   __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x3f0
-  __DATA_CONST.__cfstring: 0xb40
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x9c0
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xf28
-  __DATA.__objc_selrefs: 0xd60
-  __DATA.__objc_ivar: 0x88
-  __DATA.__objc_data: 0x280
+  __DATA.__objc_const: 0xdc8
+  __DATA.__objc_selrefs: 0xc78
+  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUI.framework/SpringBoardUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BDEAF3B-2176-3866-81C8-1E9228028D3C
-  Functions: 313
-  Symbols:   193
-  CStrings:  892
+  UUID: B5FD1506-612F-37AF-BD88-B82811347EA9
+  Functions: 278
+  Symbols:   187
+  CStrings:  820
 
Symbols:
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
- _CFPropertyListCreateDeepCopy
- _OBJC_CLASS_$_MSDHubFeatureFlags
- _OBJC_CLASS_$_NSException
- _OBJC_CLASS_$_NSPropertyListSerialization
- _OBJC_CLASS_$_NSSet
- _OBJC_METACLASS_$_MSDHubFeatureFlags
- _kCFAllocatorDefault
- _objc_getProperty
- _objc_setProperty_atomic
CStrings:
+ "1 second has passed waiting for xpc call to check type of demo device.  Moving on..."
+ "com.apple.ist.ie"
+ "isScreenDarkHoursEnabled"
+ "readPreferencesFileObjectForKey:"
- "%{public}s - Both object and key must be non-nil."
- "%{public}s - Exception:  %{public}@"
- "%{public}s - Failed to read preferences file:  %{public}@ - Error:  %{public}@"
- "%{public}s - Failed to save preferences file:  %{public}@ - Error:  %{public}@"
- "%{public}s - Key is nil."
- "%{public}s - Key must be of type NSString."
- "%{public}s - Keys array pointer is nil."
- "-[MSDPreferencesFile objectForKey:]"
- "-[MSDPreferencesFile populateCache]"
- "-[MSDPreferencesFile raiseInvalidPropertyListObjectExceptionForObject:]"
- "-[MSDPreferencesFile removeObjectForKey:]"
- "-[MSDPreferencesFile removeObjectsForKeys:]"
- "-[MSDPreferencesFile saveCache]"
- "-[MSDPreferencesFile setObject:forKey:]"
- "/private/var/mnt/com.apple.mobilestoredemo.storage/com.apple.mobilestoredemo.blob/Metadata"
- "@\"NSMutableDictionary\""
- "B32@0:8@16@24"
- "DisableBackgroundInstall"
- "DisableCleanEnergyCharging"
- "DisableNightlyLowPowerMode"
- "DisableNightlySnapshotRevert"
- "DisableScreenDarkHours"
- "DisableStudioDisplayUpdate"
- "DisableUserHomeDeepClean"
- "FeatureFlags"
- "InvalidPropertyListObject"
- "MSDHubFeatureFlags"
- "MSDPreferencesFile"
- "Object %@ of type %@ is not a valid property list object."
- "Setting preference %{public}@:%{public}@"
- "T@\"NSMutableDictionary\",&,V_cache"
- "_cache"
- "cache"
- "deepCopy:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "disableBackgroundInstall"
- "disableCleanEnergyCharging"
- "disableNightlyLowPowerMode"
- "disableNightlySnapshotRevert"
- "disableScreenDarkHours"
- "disableStudioDisplayUpdate"
- "disableUserHomeDeepClean"
- "exceptionWithName:reason:userInfo:"
- "fileURLWithPath:isDirectory:"
- "isSupportedFeatureFlag:"
- "path"
- "plist"
- "populateCache"
- "preferencesFilePath"
- "preferencesFileUrl"
- "propertyList:isValidForFormat:"
- "raise"
- "raiseInvalidPropertyListObjectExceptionForObject:"
- "readBoolValueForFeatureFlag:"
- "reload"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "saveCache"
- "setCache:"
- "setWithObjects:"
- "stringByAppendingPathExtension:"
- "supportedFeatureFlags"
- "writeToURL:error:"

```
