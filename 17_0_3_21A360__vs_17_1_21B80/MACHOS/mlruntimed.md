## mlruntimed

> `/usr/libexec/mlruntimed`

```diff

-101.0.0.0.0
-  __TEXT.__text: 0x1a0e4
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x32e0
-  __TEXT.__objc_methlist: 0x126c
+101.1.0.0.0
+  __TEXT.__text: 0x1790c
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x2f60
+  __TEXT.__objc_methlist: 0x113c
   __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0x19a8
-  __TEXT.__cstring: 0x1172
-  __TEXT.__objc_classname: 0x38c
-  __TEXT.__objc_methname: 0x3856
-  __TEXT.__objc_methtype: 0xd6c
+  __TEXT.__oslogstring: 0x16e6
+  __TEXT.__cstring: 0x1010
+  __TEXT.__objc_classname: 0x373
+  __TEXT.__objc_methname: 0x3548
+  __TEXT.__objc_methtype: 0xd48
   __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__unwind_info: 0x6c0
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0xa70
-  __DATA_CONST.__cfstring: 0xc00
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x63c
+  __DATA_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0xa50
+  __DATA_CONST.__cfstring: 0xa40
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x7860
-  __DATA.__objc_selrefs: 0xdb8
+  __DATA.__objc_const: 0x7268
+  __DATA.__objc_selrefs: 0xce0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x250
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x200
-  __DATA.__objc_data: 0x7d0
+  __DATA.__objc_classrefs: 0x240
+  __DATA.__objc_superrefs: 0x80
+  __DATA.__objc_ivar: 0x1d4
+  __DATA.__objc_data: 0x780
   __DATA.__data: 0x420
   __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5538C382-304D-3F70-960D-0CAF829D0496
-  Functions: 619
-  Symbols:   238
-  CStrings:  1130
+  UUID: 38595FCA-8EA8-32AB-AB8A-14AD28A52E24
+  Functions: 563
+  Symbols:   234
+  CStrings:  1052
 
Symbols:
- _MLRuntimePluginID_ProactiveShareSheetLighthousePFLPlugin
- _OBJC_CLASS_$_TRIDownloadOptions
- ___NSArray0__struct
- _arc4random_uniform
CStrings:
- "\x13\x16"
- "%@.fromTrial"
- "@\"TRIClient\""
- "@52@0:8@16@24@32B40@44"
- "ATTACHMENTS"
- "Adding Trial PFL task for %@"
- "Bail out since there is no matched record for plugin=%@"
- "Fail to create TRIClient with projectID=%d."
- "Fail to create TRIClient."
- "Fail to download factors for %@ with error=%@"
- "Fail to fetch policy with error=%@"
- "Fail to fetch recipe with error=%@"
- "Fail to load plugin for %@ with error=%@"
- "Fail to perform PFL task."
- "Fail to read attachmentURLs with error=%@"
- "Fail to read recipe from recipeURL=(%@), error=%@"
- "Fail to run task, bundleID=%@, recipeID=%@, error=%@"
- "Finish downloading factors for %@"
- "MLRTrialPFLTaskWorker"
- "More than one PFL task from Trial. Only supporting the first one for now."
- "No PFL tasks from Trial for %@"
- "No matched data"
- "PFL_CARRY"
- "POLICY"
- "RECIPE"
- "Start downloading factors for (%@)..."
- "Task is completed without error, plugin=%@, recipeID=%@."
- "URLForfactor:"
- "Unsupported factory type=%d"
- "_initWithAssetURL:bundleIdentifier:error:"
- "_trialClient"
- "addSkippedRecordForRecipe:description:"
- "attachmentsDirURL"
- "attachmentsWithError:"
- "canRunWithSchedulingRecord:"
- "clientWithProjectId:factorsState:"
- "com.apple.PriML.PFL"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "createTaskWorkerForTrialPFLTask:completion:"
- "defaultManager"
- "directoryValue"
- "downloadLevelsForFactors:withNamespace:queue:options:progress:completion:"
- "fileLevel.directoryValue.path for %@ is nil"
- "fileLevel.fileValue.path for %@ is nil"
- "fileURLWithPath:isDirectory:"
- "fileValue"
- "initWithAllowsCellular:discretionaryBehavior:"
- "initWithAssetURL:error:"
- "initWithPluginID:recordSet:trialManager:alwaysRun:pluginOverride:"
- "levelForFactor:withNamespaceName:"
- "levelOneOfCase"
- "loadPluginIfNecessary:"
- "nil fileLevel returned for factor=%@"
- "path for %@: (%@)"
- "plugin ID should not be nil."
- "policyURL"
- "policyWithError:"
- "projectId"
- "recipeURL"
- "recipeWithError:"
- "refresh"
- "runSynchronouslyWithCompletion:"

```
