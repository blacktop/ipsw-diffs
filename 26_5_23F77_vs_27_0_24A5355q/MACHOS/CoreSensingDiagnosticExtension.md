## CoreSensingDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/CoreSensingDiagnosticExtension.appex/CoreSensingDiagnosticExtension`

```diff

-11.28.0.0.0
-  __TEXT.__text: 0x12c
-  __TEXT.__auth_stubs: 0x80
-  __TEXT.__objc_stubs: 0x60
-  __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x40
-  __TEXT.__oslogstring: 0x2f
+20.26.0.0.1
+  __TEXT.__text: 0x718
+  __TEXT.__auth_stubs: 0x150
+  __TEXT.__objc_stubs: 0x1e0
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x38
+  __TEXT.__cstring: 0xbe
+  __TEXT.__oslogstring: 0x273
   __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x6e
-  __TEXT.__objc_methtype: 0x13
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x48
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__cfstring: 0x40
+  __TEXT.__objc_methname: 0x185
+  __TEXT.__objc_methtype: 0x1b
+  __TEXT.__unwind_info: 0x68
+  __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x28
+  __DATA.__objc_selrefs: 0x88
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 778BD43C-2F97-3D65-AE77-D973BA9CA0E8
-  Functions: 2
-  Symbols:   23
-  CStrings:  13
+  UUID: C3158B52-9507-3B24-B26E-2E004036C4B6
+  Functions: 3
+  Symbols:   40
+  CStrings:  43
 
Symbols:
+ _CFPrefs_GetDouble
+ _CFPrefs_GetInt64
+ _NSFileCreationDate
+ _NSFileModificationDate
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_release_x20
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x26
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_release_x21
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "(unknown)"
+ "CoreSensingDiagnosticExtension launched by: %@, consent: %d"
+ "CoreSensingDiagnosticExtension: Disk flush cleanup deleted %lu of %lu file(s), hoursToKeep: %g"
+ "CoreSensingDiagnosticExtension: Disk flush not enabled (err=%d), skipping cleanup"
+ "CoreSensingDiagnosticExtension: Disk flush path does not exist, returning empty attachments"
+ "CoreSensingDiagnosticExtension: Failed to delete %{public}@: %{public}@"
+ "CoreSensingDiagnosticExtension: Failed to enumerate disk flush directory: %{public}@"
+ "CoreSensingDiagnosticExtension: No consent provided, returning empty attachments"
+ "CoreSensingDiagnosticExtension: Returning %lu attachment(s)"
+ "DEExtensionAttachmentsParamConsentProvidedKey"
+ "attributesOfItemAtPath:error:"
+ "boolValue"
+ "cleanupExpiredDiskFlushFiles"
+ "com.apple.AccessorySensorManager"
+ "compare:"
+ "contentsOfDirectoryAtPath:error:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dateWithTimeIntervalSinceNow:"
+ "defaultManager"
+ "diskFlushHoursToKeep"
+ "enableDiskFlush"
+ "fileExistsAtPath:"
+ "removeItemAtPath:error:"
+ "stringByAppendingPathComponent:"
+ "v16@0:8"
- "CoreSensingDiagnosticExtension: launched by %@"

```
