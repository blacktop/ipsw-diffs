## com.apple.datamigrator

> `/System/Library/PrivateFrameworks/DataMigration.framework/XPCServices/com.apple.datamigrator.xpc/com.apple.datamigrator`

```diff

-2842.4.0.0.0
-  __TEXT.__text: 0x12694
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_stubs: 0x2f20
-  __TEXT.__objc_methlist: 0x12d4
-  __TEXT.__const: 0x80
-  __TEXT.__objc_methname: 0x3e2c
-  __TEXT.__cstring: 0x38ef
-  __TEXT.__objc_classname: 0x311
-  __TEXT.__objc_methtype: 0x7f8
-  __TEXT.__gcc_except_tab: 0x82c
+2851.0.0.0.0
+  __TEXT.__text: 0x12ed4
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_stubs: 0x3300
+  __TEXT.__objc_methlist: 0x1404
+  __TEXT.__const: 0x88
+  __TEXT.__objc_methname: 0x429f
+  __TEXT.__cstring: 0x3b64
+  __TEXT.__objc_classname: 0x301
+  __TEXT.__objc_methtype: 0x84b
+  __TEXT.__gcc_except_tab: 0x9d0
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__ustring: 0x10c
-  __TEXT.__oslogstring: 0xd6
-  __TEXT.__unwind_info: 0x558
-  __DATA_CONST.__auth_got: 0x4f0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x28c0
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__oslogstring: 0xfe
+  __TEXT.__unwind_info: 0x520
+  __DATA_CONST.__const: 0x8e0
+  __DATA_CONST.__cfstring: 0x2a60
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_arraydata: 0xb10
-  __DATA_CONST.__objc_dictobj: 0x938
+  __DATA_CONST.__objc_arraydata: 0xb78
+  __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3030
-  __DATA.__objc_selrefs: 0xe50
-  __DATA.__objc_ivar: 0x1a4
-  __DATA.__objc_data: 0x7d0
+  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0x1a8
+  __DATA.__objc_const: 0x3240
+  __DATA.__objc_selrefs: 0xf48
+  __DATA.__objc_ivar: 0x1c4
+  __DATA.__objc_data: 0x820
   __DATA.__data: 0x190
   __DATA.__bss: 0x118
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C2D9AC2-54DA-3EE9-A837-A7B5626F0708
-  Functions: 444
-  Symbols:   300
-  CStrings:  1500
+  UUID: 17206D19-FD70-37D2-87AE-874FEDBCF1A0
+  Functions: 470
+  Symbols:   307
+  CStrings:  1581
 
Symbols:
+ _DMPreboardModeDescription
+ _OBJC_CLASS_$_DMTraceCollector
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_METACLASS_$_DMTraceCollector
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _xpc_dictionary_set_double
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
CStrings:
+ "@\"BKSAlternateSystemApp\""
+ "@\"DMHelperConnection\""
+ "@\"NSDateFormatter\""
+ "@40@0:8@16@24B32B36"
+ "Added plugin %@ to current trace."
+ "DMMigratorProxy did send response for event %p msgID %@ to client pid %@ (mode: %@)"
+ "DMTrace.%@.%@.atrc"
+ "DMTraceCollector"
+ "Did load keybag created by Preboard with result %@"
+ "Done waiting for concurrent plugins to start."
+ "Ending tracing for plugin %@"
+ "Launching Preboard"
+ "Launching Preboard with mode %{public}@"
+ "Plugin identifier %@ is already being traced."
+ "Starting trace for plugin %@"
+ "Stopping trace with filename: %@ for plugins: %@"
+ "T@\"BKSAlternateSystemApp\",&,V_preboardApp"
+ "T@\"DMEnvironment\",&,V_environment"
+ "T@\"DMHelperConnection\",&,V_helperConnection"
+ "T@\"NSDateFormatter\",&,V_dateFormatter"
+ "T@\"NSMutableArray\",&,V_activePluginsInCurrentTrace"
+ "T@\"NSMutableArray\",&,V_completedPluginsInCurrentTrace"
+ "TB,R,N,V_isConcurrent"
+ "TI,V_requiredPreboardMode"
+ "Terminating Preboard"
+ "Will attempt to load keybag created by Preboard"
+ "Will wait for remaining concurrent plugins to start."
+ "_activePluginsInCurrentTrace"
+ "_completedPluginsInCurrentTrace"
+ "_createTraceCollector"
+ "_dateFormatter"
+ "_helperConnection"
+ "_internalBuild"
+ "_isConcurrent"
+ "_preboardApp"
+ "_requiredPreboardMode"
+ "_traceFileNameForPluginIdentifiers:"
+ "_tracingEnabledForPlugin:"
+ "activePluginsInCurrentTrace"
+ "array"
+ "broadcast"
+ "com.apple.SecureSettingsMigrationKit.migrator"
+ "com.apple.datamigrator.concurrentPluginExecutorQueue"
+ "com.apple.datamigrator.requiredPreboardMode"
+ "combined"
+ "completedPluginsInCurrentTrace"
+ "dateFormatter"
+ "dependent on %@"
+ "dmps_pluginDependencyIdentifier"
+ "endTracingWithFilename:"
+ "filename"
+ "full"
+ "helperConnection"
+ "initWithHelperConnection:environment:"
+ "initWithIdentifier:fileSystemRep:isUserAgnostic:isConcurrent:"
+ "isDarkBoot"
+ "isFullTracingEnabled"
+ "isTracingEnabledForAllPlugins"
+ "isTracingEnabledForPluginIdentifier:"
+ "preboardApp"
+ "preboardMode"
+ "removeObjectAtIndex:"
+ "requiredPreboardMode"
+ "set"
+ "setActivePluginsInCurrentTrace:"
+ "setCompletedPluginsInCurrentTrace:"
+ "setDateFormatter:"
+ "setHelperConnection:"
+ "setPreboardApp:"
+ "setRequiredPreboardMode:"
+ "startTraceWithDuration:fullTrace:"
+ "startTracingIfNecessaryForPlugin:"
+ "stopTracing called for plugin not being currently traced: %@"
+ "stopTracingIfNecessaryForPlugin:"
+ "traceDuration"
+ "v28@0:8d16B24"
+ "wait"
+ "yyyy-MM-dd-HH-mm-ss"
- "@36@0:8@16@24B32"
- "Did load keybag created by PreBoard with result %@"
- "TB,R,D,N"
- "Unlocked. Continuing..."
- "Waiting for user unlock"
- "We need to unlock the device. Bringing up the unlock screen..."
- "Will attempt to load keybag created by PreBoard"
- "dmps_concurrentPluginDependencyIdentifier"
- "initWithIdentifier:fileSystemRep:isUserAgnostic:"
- "\x864"

```
