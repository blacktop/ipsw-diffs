## NanoComplicationSettings

> `/System/Library/PrivateFrameworks/NanoComplicationSettings.framework/NanoComplicationSettings`

```diff

 19.0.0.0.0
-  __TEXT.__text: 0x2af0
-  __TEXT.__auth_stubs: 0x380
+  __TEXT.__text: 0x2c40
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x251
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x188
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x9fa
   __TEXT.__objc_methtype: 0x100

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2d0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x4b0

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F5AD642-6084-3313-A368-4DEF45193F40
+  UUID: 9F7C7314-0FCB-3DA3-B620-FA07F7BEFB65
   Functions: 81
-  Symbols:   391
+  Symbols:   387
   CStrings:  179
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[NCSInternalSettingsManager selectedComplicationIdentifier] : 144 -> 156
~ -[NCSInternalSettingsManager setSelectedComplicationIdentifier:] : 236 -> 244
~ -[NCSInternalSettingsManager addComplicationDefinition:] : 152 -> 160
~ -[NCSInternalSettingsManager removeComplicationDefinitionsInArray:] : 172 -> 168
~ ___73-[NCSInternalSettingsManager enumerateComplicationDefinitionsUsingBlock:]_block_invoke : 120 -> 128
~ -[NCSInternalSettingsManager enumerateAllComplicationDefinitionsUsingBlock:] : 356 -> 352
~ ___74-[NCSInternalSettingsManager moveComplicationDefinitionFromIndex:toIndex:]_block_invoke : 120 -> 124
~ -[NCSInternalSettingsManager complicationDefinitionForAppBundleIdentifier:] : 308 -> 300
~ ___75-[NCSInternalSettingsManager complicationDefinitionForAppBundleIdentifier:]_block_invoke : 152 -> 164
~ -[NCSInternalSettingsManager complicationDefinitionForComplicationIdentifier:] : 308 -> 300
~ ___78-[NCSInternalSettingsManager complicationDefinitionForComplicationIdentifier:]_block_invoke : 152 -> 164
~ -[NCSInternalSettingsManager complicationDefinitionForWatchKitIdentifier:] : 308 -> 300
~ ___74-[NCSInternalSettingsManager complicationDefinitionForWatchKitIdentifier:]_block_invoke : 152 -> 164
~ -[NCSInternalSettingsManager _saveSettings] : 492 -> 504
~ -[NCSInternalSettingsManager complicationIdentifierForComplicationDefinitionAtIndex:] : 284 -> 288
~ ___85-[NCSInternalSettingsManager complicationIdentifierForComplicationDefinitionAtIndex:]_block_invoke : 84 -> 88
~ ___42-[NCSInternalSettingsManager loadSettings]_block_invoke : 644 -> 684
~ +[NSDictionary(NCSComplication) dictionaryWithComplication:] : 416 -> 452
~ -[NCSComplication initWithDictionary:] : 368 -> 392
~ -[NCSComplication complicationIdentifier] : 100 -> 120
~ -[NCSComplication copyWithZone:] : 256 -> 272
~ +[NCSSettingsManager sharedSettingsManager] : 68 -> 84
~ -[NCSSettingsManager init] : 332 -> 336
~ -[NCSSettingsManager dealloc] : 184 -> 188
~ -[NCSSettingsManager setDelegate:] : 168 -> 172
~ -[NCSSettingsManager loadSettings] : 116 -> 120
~ -[NCSSettingsManager _updateSockPuppetComplications] : 448 -> 452
~ ___52-[NCSSettingsManager _updateSockPuppetComplications]_block_invoke : 488 -> 540
~ -[NCSSettingsManager _fetchSockPuppetComplications] : 764 -> 748
~ ___51-[NCSSettingsManager _fetchSockPuppetComplications]_block_invoke_2 : 96 -> 112
~ ___51-[NCSSettingsManager _fetchSockPuppetComplications]_block_invoke_4 : 96 -> 112
~ ___51-[NCSSettingsManager _fetchSockPuppetComplications]_block_invoke_5 : 608 -> 640

```
