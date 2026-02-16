## ContactsMetrics

> `/System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics`

```diff

-21.200.2.0.0
-  __TEXT.__text: 0x1108
-  __TEXT.__auth_stubs: 0x250
+21.500.21.0.0
+  __TEXT.__text: 0x11ac
+  __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_methlist: 0x3a4
   __TEXT.__cstring: 0x9c7
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__oslogstring: 0x20
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0xac
   __TEXT.__objc_methname: 0x63b
   __TEXT.__objc_methtype: 0x1eb

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x228
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x120
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xea0
   __AUTH_CONST.__objc_const: 0x710

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25CE0500-F604-32FC-AF47-6EED08895F78
+  UUID: 98277E16-D498-3627-9246-1FDB8A9ADDAD
   Functions: 43
-  Symbols:   366
+  Symbols:   363
   CStrings:  365
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
Functions:
~ -[CNMetricsUIReporter logSearchResultsFetchedforApplication:fromSuggestions:] : 292 -> 300
~ -[CNMetricsUIReporter logSearchResultsSelectedforApplication:fromSuggestions:] : 292 -> 300
~ -[CNMetricsUIReporter logUnknownContactGeminiViewDifferentChannelSelected:] : 244 -> 252
~ +[CNMetricsReporter log] : 68 -> 84
~ +[CNMetricsReporter sendDictionary:forEvent:andLog:] : 128 -> 124
~ ___52-[CNMetricsReporter sendDictionary:forEvent:andLog:]_block_invoke : 8 -> 56
~ -[CNMetricsReporter compoundKeyForEvent:] : 108 -> 116
~ +[CNMetricsReporter logDatabaseResolution:] : 216 -> 220
~ -[CNMetricsReporterSpiedEntry initWithDictionary:event:logged:] : 172 -> 168
~ -[CNMetricsReporterSpiedEntry description] : 176 -> 184
~ -[CNMetricsReporterSpiedEntry copyWithZone:] : 4 -> 40
~ -[CNMetricsReporterSpiedEntry initWithCoder:] : 256 -> 268
~ -[CNMetricsReporterSpiedEntry encodeWithCoder:] : 128 -> 136
~ -[CNMetricsReporterSpy events] : 104 -> 108
~ -[CNMetricsReporterSpy clearEvents] : 108 -> 112

```
