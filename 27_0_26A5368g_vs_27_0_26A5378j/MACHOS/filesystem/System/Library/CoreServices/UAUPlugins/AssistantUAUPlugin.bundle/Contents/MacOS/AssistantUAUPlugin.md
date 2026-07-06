## AssistantUAUPlugin

> `/System/Library/CoreServices/UAUPlugins/AssistantUAUPlugin.bundle/Contents/MacOS/AssistantUAUPlugin`

```diff

-  __TEXT.__text: 0x8c
-  __TEXT.__auth_stubs: 0x40
-  __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x184
-  __TEXT.__cstring: 0x34
+  __TEXT.__text: 0x878
+  __TEXT.__auth_stubs: 0x110
+  __TEXT.__objc_stubs: 0x1a0
+  __TEXT.__objc_methlist: 0x1ac
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x117
+  __TEXT.__oslogstring: 0x3ae
+  __TEXT.__ustring: 0x34
   __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x1f4
+  __TEXT.__objc_methname: 0x2f3
   __TEXT.__objc_methtype: 0xeb
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__cfstring: 0x60
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x28
+  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x220
-  __DATA.__objc_selrefs: 0xe0
+  __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2
-  Symbols:   12
-  CStrings:  58
+  Functions: 13
+  Symbols:   33
+  CStrings:  95
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _AFAppAccessMigratorShouldRun
+ _AFNeedsLegacyAssistantEnabledRemoval
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFPreferencesCopyAppValue
+ _CFRelease
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSTask
+ _OBJC_CLASS_$_NSURL
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ ___NSArray0__struct
+ __os_feature_enabled_impl
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_once
+ _objc_alloc_init
+ _objc_retainAutoreleaseReturnValue
+ _os_log_create
+ _os_log_type_enabled
CStrings:
+ "(nil — new/migrated user)"
+ "(unknown)"
+ "/System/Library/CoreServices/SiriAppAccessMigrator"
+ "27.0"
+ "App Access migration: NSTask launch of siri-app-access-migrator failed: %{public}@. Migration will retry on next login."
+ "App Access migration: SiriSetup/restrict_access_ui FF disabled — skipping (will retry on next login)."
+ "App Access migration: launched siri-app-access-migrator (pid %d) fire-and-forget; returning to login."
+ "App Access migration: new or freshly-migrated user account (nil previousOSVersion) — will run."
+ "App Access migration: performed-flag already set in user prefs — skipping."
+ "App Access migration: previous OS %{public}@ < cutoff %{public}@ — will run."
+ "App Access migration: previous OS %{public}@ >= cutoff %{public}@ — already past Rave-A boundary, skipping."
+ "App Access migration: siri-app-access-migrator tool not found or not executable at %{public}@; cannot run migration. Migration will retry on next login."
+ "AppAccessExclusionListMigrationPerformed"
+ "AppAccessMigrator"
+ "Evaluating App Access migration inclusion. previousOSVersion=%{public}@ currentOSVersion=%{public}@"
+ "SiriSetup"
+ "_isAppAccessMigrationAlreadyPerformed"
+ "_launchAppAccessMigratorTool"
+ "_shouldRunAppAccessMigrationForParameters:"
+ "com.apple.assistant"
+ "com.apple.siri"
+ "currentOSVersion"
+ "defaultManager"
+ "fileURLWithPath:"
+ "isExecutableFileAtPath:"
+ "launchAndReturnError:"
+ "processIdentifier"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "restrict_access_ui"
+ "setArguments:"
+ "setExecutableURL:"
+ "v8@?0"

```
