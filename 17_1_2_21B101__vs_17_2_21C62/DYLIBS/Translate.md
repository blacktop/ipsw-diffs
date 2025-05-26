## Translate

> `/System/Library/AccessibilityBundles/Translate.axbundle/Translate`

```diff

-2909.1.4.3.0
-  __TEXT.__text: 0x11a0
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_methlist: 0x220
-  __TEXT.__cstring: 0x4af
+2909.1.4.13.0
+  __TEXT.__text: 0x1464
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_methlist: 0x2b8
+  __TEXT.__cstring: 0x57f
+  __TEXT.__oslogstring: 0x7c
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xdc
-  __TEXT.__objc_classname: 0x1e3
-  __TEXT.__objc_methname: 0x4d3
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_classname: 0x273
+  __TEXT.__objc_methname: 0x56b
   __TEXT.__objc_methtype: 0x41
-  __TEXT.__objc_stubs: 0x3c0
-  __DATA_CONST.__got: 0x20
+  __TEXT.__objc_stubs: 0x400
+  __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3a8
-  __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_const: 0x4c8
+  __DATA_CONST.__objc_selrefs: 0x188
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x3a8
-  __AUTH_CONST.__auth_got: 0xf0
-  __DATA.__objc_classrefs: 0x50
+  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__objc_const: 0x4c8
+  __AUTH_CONST.__auth_got: 0x108
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_classrefs: 0x58
   __DATA.__objc_superrefs: 0x28
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 45
-  Symbols:   245
-  CStrings:  118
+  Functions: 54
+  Symbols:   291
+  CStrings:  136
 
Symbols:
+ +[LanguageAwareTextViewAccessibility _accessibilityPerformValidations:]
+ +[LanguageAwareTextViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[LanguageAwareTextViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[RecordingHelperAccessibility _accessibilityPerformValidations:]
+ +[RecordingHelperAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[RecordingHelperAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[LanguageAwareTextViewAccessibility accessibilityLanguage]
+ -[RecordingHelperAccessibility _accessibilityDidStartListening]
+ -[RecordingHelperAccessibility _accessibilityDidStopListening]
+ _AXLogCommon
+ _OBJC_CLASS_$_LanguageAwareTextViewAccessibility
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_RecordingHelperAccessibility
+ _OBJC_CLASS_$___LanguageAwareTextViewAccessibility_super
+ _OBJC_CLASS_$___RecordingHelperAccessibility_super
+ _OBJC_METACLASS_$_LanguageAwareTextViewAccessibility
+ _OBJC_METACLASS_$_RecordingHelperAccessibility
+ _OBJC_METACLASS_$___LanguageAwareTextViewAccessibility_super
+ _OBJC_METACLASS_$___RecordingHelperAccessibility_super
+ _UIApp
+ __OBJC_$_CLASS_METHODS_LanguageAwareTextViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_RecordingHelperAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_LanguageAwareTextViewAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_RecordingHelperAccessibility(SafeCategory)
+ __OBJC_CLASS_RO_$_LanguageAwareTextViewAccessibility
+ __OBJC_CLASS_RO_$_RecordingHelperAccessibility
+ __OBJC_CLASS_RO_$___LanguageAwareTextViewAccessibility_super
+ __OBJC_CLASS_RO_$___RecordingHelperAccessibility_super
+ __OBJC_METACLASS_RO_$_LanguageAwareTextViewAccessibility
+ __OBJC_METACLASS_RO_$_RecordingHelperAccessibility
+ __OBJC_METACLASS_RO_$___LanguageAwareTextViewAccessibility_super
+ __OBJC_METACLASS_RO_$___RecordingHelperAccessibility_super
+ ___kCFBooleanTrue
+ __os_log_impl
+ _objc_msgSend$_accessibilitySetIsDictationListeningOverride:
+ _objc_msgSend$localeIdentifier
+ _os_log_type_enabled
CStrings:
+ "Finished recording for Translation. Resetting VO quiet state."
+ "LanguageAwareTextViewAccessibility"
+ "Marking VO to be quiet since we are recording for Translation"
+ "RecordingHelperAccessibility"
+ "SequoiaTranslator.LanguageAwareTextView"
+ "SequoiaTranslator.RecordingHelper"
+ "__LanguageAwareTextViewAccessibility_super"
+ "__RecordingHelperAccessibility_super"
+ "_accessibilityDidStartListening"
+ "_accessibilityDidStopListening"
+ "_accessibilitySetIsDictationListeningOverride:"
+ "accessibilityLanguage"
+ "locale"
+ "localeIdentifier"

```
