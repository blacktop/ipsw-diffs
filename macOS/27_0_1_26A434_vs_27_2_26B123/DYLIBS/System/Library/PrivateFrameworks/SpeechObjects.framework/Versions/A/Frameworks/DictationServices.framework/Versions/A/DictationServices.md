## DictationServices

> `/System/Library/PrivateFrameworks/SpeechObjects.framework/Versions/A/Frameworks/DictationServices.framework/Versions/A/DictationServices`

```diff

-6.1.89.0.0
-  __TEXT.__text: 0x4f33c
-  __TEXT.__objc_methlist: 0x5e94
+6.1.89.2.0
+  __TEXT.__text: 0x501a8
+  __TEXT.__objc_methlist: 0x5f14
   __TEXT.__const: 0x398
-  __TEXT.__gcc_except_tab: 0xbc4
-  __TEXT.__cstring: 0x59d6
+  __TEXT.__gcc_except_tab: 0xc30
+  __TEXT.__cstring: 0x5b6c
   __TEXT.__oslogstring: 0x15ed
   __TEXT.__ustring: 0x9c
-  __TEXT.__unwind_info: 0x17a0
+  __TEXT.__unwind_info: 0x17c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4618
-  __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x7d0
-  __AUTH_CONST.__const: 0x1300
-  __AUTH_CONST.__cfstring: 0x4a20
+  __DATA_CONST.__objc_selrefs: 0x4690
+  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_arraydata: 0x180
+  __DATA_CONST.__got: 0x7e8
+  __AUTH_CONST.__const: 0x1350
+  __AUTH_CONST.__cfstring: 0x4c80
   __AUTH_CONST.__objc_const: 0xe908
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__auth_got: 0x7d8
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x2030
   __DATA.__objc_ivar: 0x7a4
   __DATA.__data: 0x838
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x4b8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/Versions/A/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/AccessibilitySupport
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2242
-  Symbols:   5849
-  CStrings:  889
+  Functions: 2255
+  Symbols:   5886
+  CStrings:  910
 
Symbols:
+ +[SOApplicationUtilities _localizedNameForAppBundle:]
+ +[SOOverlayWindow _absoluteLevelSpace]
+ -[DSRMessageTracerUtilities .cxx_destruct]
+ -[DSRMessageTracerUtilities bucketizePixelCount:]
+ -[DSRMessageTracerUtilities displayCount]
+ -[DSRMessageTracerUtilities effectiveResolutionPixelCount:]
+ -[DSRMessageTracerUtilities isBuiltIn:]
+ -[DSRMessageTracerUtilities isClamshellClosed]
+ -[DSRMessageTracerUtilities isMainDisplay:]
+ -[DSRMessageTracerUtilities logDisplayAnalytics]
+ GCC_except_table12
+ _AnalyticsSendEventLazy
+ _CGDisplayIsBuiltin
+ _CGSAddWindowsToSpaces
+ _CGSShowSpaces
+ _CGSSpaceCreate
+ _CGSSpaceSetAbsoluteLevel
+ __48-[DSRMessageTracerUtilities logDisplayAnalytics]_block_invoke
+ __OBJC_$_CLASS_METHODS_SOOverlayWindow
+ ___38+[SOOverlayWindow _absoluteLevelSpace]_block_invoke
+ ___48-[DSRMessageTracerUtilities logDisplayAnalytics]_block_invoke
+ ___block_descriptor_40_e8_32w_e19_"NSDictionary"8?0l
+ _absoluteLevelSpace.onceToken
+ _absoluteLevelSpace.sSpace
+ _kCGSWorkspaceIdentifierKey
+ _kCGSWorkspaceTypeKey
+ _kSLSSpaceAbsoluteLevelVoiceOver
+ _objc_msgSend$CGDirectDisplayID
+ _objc_msgSend$URLForResource:withExtension:subdirectory:localization:
+ _objc_msgSend$_absoluteLevelSpace
+ _objc_msgSend$_localizedNameForAppBundle:
+ _objc_msgSend$bucketizePixelCount:
+ _objc_msgSend$bundlePath
+ _objc_msgSend$deviceDescription
+ _objc_msgSend$dictionaryWithContentsOfURL:
+ _objc_msgSend$displayCount
+ _objc_msgSend$effectiveResolutionPixelCount:
+ _objc_msgSend$isBuiltIn:
+ _objc_msgSend$isMainDisplay:
+ _objc_msgSend$localizedInfoDictionary
+ _objc_msgSend$objectForInfoDictionaryKey:
+ _objc_msgSend$preferredLanguages
- -[DSRMessageTracerUtilities dealloc]
- GCC_except_table14
- GCC_except_table28
- GCC_except_table29
- _objc_msgSend$initWithFormat:
CStrings:
+ "&A\""
+ "@\"NSDictionary\"8@?0"
+ "CFBundleDisplayName"
+ "CFBundleName"
+ "CFBundleVisibleComponentName"
+ "DictationLabeledElementsOverlayMultiMonitor"
+ "DisplayCount"
+ "InfoPlist"
+ "IsClamshellClosed"
+ "NSScreenNumber"
+ "_NSURLIsHiddenBySystemKey"
+ "bucketedPixelCount"
+ "com.apple.Siri"
+ "com.apple.SiriApp"
+ "com.apple.SiriNCService"
+ "com.apple.campo"
+ "com.apple.message.DisplayAnalytics"
+ "com.apple.message.ScreenAnalytics"
+ "isBuiltIn"
+ "isMainDisplay"
+ "loctable"
```
