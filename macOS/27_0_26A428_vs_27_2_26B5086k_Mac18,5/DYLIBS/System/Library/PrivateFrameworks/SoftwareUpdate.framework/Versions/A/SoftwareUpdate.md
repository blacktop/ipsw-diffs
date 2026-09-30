## SoftwareUpdate

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate`

```diff

-2412.1.1.0.0
-  __TEXT.__text: 0x7a910
-  __TEXT.__objc_methlist: 0x64ac
+2412.40.11.0.0
+  __TEXT.__text: 0x798dc
+  __TEXT.__objc_methlist: 0x640c
   __TEXT.__const: 0x670
-  __TEXT.__gcc_except_tab: 0x12a8
-  __TEXT.__cstring: 0x8482
-  __TEXT.__oslogstring: 0xb49c
+  __TEXT.__gcc_except_tab: 0x1274
+  __TEXT.__cstring: 0x8389
+  __TEXT.__oslogstring: 0xb366
   __TEXT.__dof_SoftwareU: 0xc20
-  __TEXT.__unwind_info: 0x2fc0
+  __TEXT.__unwind_info: 0x2f50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x9d8
+  __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f48
+  __DATA_CONST.__objc_selrefs: 0x3f40
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x718
+  __DATA_CONST.__got: 0x710
   __AUTH_CONST.__const: 0x29e0
-  __AUTH_CONST.__cfstring: 0x73c0
-  __AUTH_CONST.__objc_const: 0x8940
+  __AUTH_CONST.__cfstring: 0x7360
+  __AUTH_CONST.__objc_const: 0x8880
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_got: 0x800
-  __AUTH.__objc_data: 0x780
+  __AUTH.__objc_data: 0x730
   __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x5c0
   __DATA_DIRTY.__objc_data: 0xe60

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 3204
-  Symbols:   6317
-  CStrings:  1981
+  Functions: 3182
+  Symbols:   6277
+  CStrings:  1967
 
Symbols:
+ -[SUTelemetryPreferencesEvent _appendBootPolicyTelemetryToDict:]
+ -[SUTelemetryPreferencesEvent _diagnosticsAndUsageEnabled]
+ -[SUTelemetryPreferencesEvent bootPolicyUtil]
+ -[SUTelemetryPreferencesEvent initWithBootPolicyUtil:sharedPrefs:]
+ -[SUTelemetryPreferencesEvent setBootPolicyUtil:]
+ GCC_except_table114
+ GCC_except_table123
+ GCC_except_table200
+ GCC_except_table49
+ GCC_except_table63
+ GCC_except_table72
+ OBJC_IVAR_$_SUTelemetryPreferencesEvent._bootPolicyUtil
+ OBJC_IVAR_$_SUUpdateServiceClient._entitledClient
+ _objc_msgSend$_appendBootPolicyTelemetryToDict:
+ _objc_msgSend$_diagnosticsAndUsageEnabled
+ _objc_msgSend$setBootPolicyUtil:
- +[SUTelemetryManager advancedPreferencesEvent]
- -[SUBackgroundManager installStatus:didChangeExternallyForProductKey:]
- -[SUSharedPrefs isCatalogURLManaged]
- -[SUTelemetryAdvancedPreferencesEvent _byteForNVRAMKey:namespace:]
- -[SUTelemetryAdvancedPreferencesEvent bootPolicyUtil]
- -[SUTelemetryAdvancedPreferencesEvent createReportableDictionary]
- -[SUTelemetryAdvancedPreferencesEvent eventName]
- -[SUTelemetryAdvancedPreferencesEvent initWithBootPolicyUtil:sharedPrefs:]
- -[SUTelemetryAdvancedPreferencesEvent init]
- -[SUTelemetryAdvancedPreferencesEvent setBootPolicyUtil:]
- -[SUTelemetryAdvancedPreferencesEvent setSharedPrefs:]
- -[SUTelemetryAdvancedPreferencesEvent sharedPrefs]
- -[SUTelemetryAdvancedPreferencesEvent telemetryServer]
- -[SUUpdateServiceClient clearInvalidationForIdentifier:version:forReason:]
- -[SUUpdateServiceClient installStatus:didChangeExternallyForProductKey:]
- -[SUUpdateServiceDaemon clearInvalidationForIdentifier:version:forReason:]
- -[SUUpdateServiceDaemon installStatus:didChangeExternallyForProductKey:]
- GCC_except_table118
- GCC_except_table126
- GCC_except_table127
- GCC_except_table204
- GCC_except_table56
- OBJC_IVAR_$_SUTelemetryAdvancedPreferencesEvent._bootPolicyUtil
- OBJC_IVAR_$_SUTelemetryAdvancedPreferencesEvent._sharedPrefs
- _OBJC_CLASS_$_SUTelemetryAdvancedPreferencesEvent
- _OBJC_METACLASS_$_SUTelemetryAdvancedPreferencesEvent
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicyAUXI
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicyAUXP
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicyAUXR
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicyCOIH
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySIP0
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySIP1
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySIP2
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySIP3
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySMB2
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySMB3
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySecurityMode
- _SUTelemetryAdvancedPreferencesEventKeyBootPolicySupported
- _SUTelemetryEventTypeCoreAnalyticsPreferences
- _SUTelemetryPreferencesEventKeyBootPolicyCount
- __70-[SUBackgroundManager installStatus:didChangeExternallyForProductKey:]_block_invoke
- __OBJC_$_INSTANCE_METHODS_SUTelemetryAdvancedPreferencesEvent
- __OBJC_$_INSTANCE_VARIABLES_SUTelemetryAdvancedPreferencesEvent
- __OBJC_$_PROP_LIST_SUTelemetryAdvancedPreferencesEvent
- __OBJC_CLASS_RO_$_SUTelemetryAdvancedPreferencesEvent
- __OBJC_METACLASS_RO_$_SUTelemetryAdvancedPreferencesEvent
- ___70-[SUBackgroundManager installStatus:didChangeExternallyForProductKey:]_block_invoke
- ___72-[SUUpdateServiceDaemon installStatus:didChangeExternallyForProductKey:]_block_invoke
- ___74-[SUUpdateServiceDaemon clearInvalidationForIdentifier:version:forReason:]_block_invoke
- _objc_msgSend$_pushProductToStage:
- _objc_msgSend$_reevaluateAvailableUpdatesIfNecessary
- _objc_msgSend$advancedPreferencesEvent
- _objc_msgSend$installStatus:didChangeExternallyForProductKey:
- _objc_msgSend$isUserPreferenceManaged:usingManaged:
- _objc_msgSend$registerProductExternallyChanged:
- _objc_msgSend$updateStatusChangedExternally:
CStrings:
+ "%s: Rejecting connection from unentitled client: %@"
+ "-[SUUpdateServiceClient stashURLCredential:]"
+ "com.apple.private.SoftwareUpdate.Client"
- "%s: %@ - new state: %@"
- "%s: Major OS deferral is disabled"
- "%s: Minor OS deferral is disabled"
- "%s: Non OS deferral is disabled"
- "%s: Period: %@"
- "-[SUBackgroundManager installStatus:didChangeExternallyForProductKey:]_block_invoke"
- "-[SUSharedPrefs majorOSDeferralPeriod]"
- "-[SUSharedPrefs minorOSDeferralPeriod]"
- "-[SUSharedPrefs nonOSDeferralPeriod]"
- "Install status changed externally for product: %@"
- "ManagedDisableSplat"
- "ManagedDisableSplatRollback"
- "Product %@ has error and will not advance states.  Error: %@"
- "Product %@ has state %@ and will not advance states"
- "Product %@ not found after install status changed externally"
- "com.apple.SoftwareUpdate.Preferences"
- "restrict-software-update-require-admin-to-install"
```
