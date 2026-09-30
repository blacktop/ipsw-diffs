## SnippetServiceUIPlugin

> `/System/Library/Snippets/UIPlugins/SnippetServiceUIPlugin.bundle/Contents/MacOS/SnippetServiceUIPlugin`

```diff

-  __TEXT.__text: 0x83680
-  __TEXT.__auth_stubs: 0x3970
-  __TEXT.__objc_stubs: 0x10a0
+  __TEXT.__text: 0x8c49c
+  __TEXT.__auth_stubs: 0x3a60
+  __TEXT.__objc_stubs: 0x10c0
   __TEXT.__objc_methlist: 0xa98
-  __TEXT.__const: 0x6338
-  __TEXT.__swift5_typeref: 0xad67
-  __TEXT.__swift5_capture: 0xef0
-  __TEXT.__swift5_reflstr: 0x1183
-  __TEXT.__swift5_assocty: 0x638
-  __TEXT.__constg_swiftt: 0x1cf4
-  __TEXT.__swift5_fieldmd: 0x13d0
-  __TEXT.__oslogstring: 0x1332
-  __TEXT.__swift5_proto: 0x220
-  __TEXT.__swift5_types: 0x228
+  __TEXT.__const: 0x6490
+  __TEXT.__swift5_typeref: 0xb281
+  __TEXT.__swift5_capture: 0x1160
+  __TEXT.__swift5_reflstr: 0x11d3
+  __TEXT.__swift5_assocty: 0x650
+  __TEXT.__constg_swiftt: 0x1d34
+  __TEXT.__swift5_fieldmd: 0x145c
+  __TEXT.__oslogstring: 0x1e70
+  __TEXT.__swift5_proto: 0x224
+  __TEXT.__swift5_types: 0x230
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__cstring: 0x16b3
-  __TEXT.__swift_as_entry: 0x94
-  __TEXT.__swift_as_cont: 0xd8
-  __TEXT.__swift_as_ret: 0x88
+  __TEXT.__cstring: 0x1633
+  __TEXT.__swift_as_entry: 0x98
+  __TEXT.__swift_as_cont: 0xe4
+  __TEXT.__swift_as_ret: 0x8c
   __TEXT.__objc_methname: 0x2496
+  __TEXT.__objc_methtype: 0x1281
   __TEXT.__objc_classname: 0x325
-  __TEXT.__objc_methtype: 0x129b
-  __TEXT.__unwind_info: 0x1fd0
-  __TEXT.__eh_frame: 0x1e34
-  __DATA_CONST.__const: 0x37b0
+  __TEXT.__unwind_info: 0x20e0
+  __TEXT.__eh_frame: 0x1e94
+  __DATA_CONST.__const: 0x3e88
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__auth_got: 0x1cc0
-  __DATA_CONST.__got: 0xc20
-  __DATA_CONST.__auth_ptr: 0x1ab0
-  __DATA.__objc_const: 0xce0
-  __DATA.__objc_selrefs: 0x9d8
-  __DATA.__objc_data: 0x5d0
-  __DATA.__data: 0x42f8
-  __DATA.__bss: 0x49b8
-  __DATA.__common: 0x78
+  __DATA_CONST.__auth_got: 0x1d38
+  __DATA_CONST.__got: 0xc80
+  __DATA_CONST.__auth_ptr: 0x1b00
+  __DATA.__objc_const: 0xd20
+  __DATA.__objc_selrefs: 0x9e0
+  __DATA.__objc_data: 0x5e0
+  __DATA.__data: 0x43e0
+  __DATA.__bss: 0x4aa8
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3643
-  Symbols:   253
-  CStrings:  702
+  Functions: 3815
+  Symbols:   256
+  CStrings:  738
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__objc_methname : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _OBJC_CLASS_$_RFBinaryButtonCardSection
+ _OBJC_CLASS_$_RFButtonCardSection
+ _OBJC_CLASS_$_RFMultiButtonCardSection
+ _OBJC_CLASS_$_SFPerformEntityQueryCommand
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "#ActionableRow: dispatch via disambiguationDescriptor"
+ "#ActionableRow: dispatch via launchApp bundleId=%s"
+ "#ActionableRow: dispatch via openFile"
+ "#ActionableRow: dispatch via prescribedAction"
+ "#ActionableRow: tapped action=%s"
+ "#AlbumPickerView album picked, sending disambiguation action albumIndex=%ld"
+ "#AlbumPickerView no matching album index for selection, matchedCount=%ld"
+ "#AppInstallationChecker: check bundleId=%s installed=%{bool}d"
+ "#AppInstallationChecker: empty bundleId, treating as not installed installed=%{bool}d"
+ "#ArchivedViewIntentExecutor: bundleIds resolved appBundleId=%s extensionBundleId=%s usedMetadataApp=%{bool}d"
+ "#ArchivedViewIntentExecutor: dropping tap, linkAction is not an LNAction"
+ "#ArchivedViewIntentExecutor: dropping tap, no app bundle identifier resolved"
+ "#ArchivedViewIntentExecutor: starting workflow runner"
+ "#ArchivedViewIntentExecutor: workflow finished cancelled=%{bool}d"
+ "#ArchivedViewIntentExecutor: workflow finished with error domain=%s code=%ld cancelled=%{bool}d"
+ "#AttributionView: tapped posting notification name=%s"
+ "#BasicInternalErrorView error view shown domain=%s"
+ "#ButtonView: dispatch via launchApp bundleId=%s"
+ "#ButtonView: dispatch via prescribedAction action=%s"
+ "#ButtonView: dispatch via showMore"
+ "#ButtonView: failed to build prescribed action action=%s errorDomain=%s errorCode=%ld"
+ "#ButtonView: tapped action=%s"
+ "#CommandThrottle: command DROPPED throttling=%{bool}d"
+ "#CommandThrottle: command allowed throttling=%{bool}d"
+ "#ConfirmationButtonView: tapped role=primary"
+ "#ConfirmationButtonView: tapped role=secondary"
+ "#FeedbackButtonView: feedback submitted type=%s"
+ "#FileThumbnailView: QL thumbnail generation failed types=%lu domain=%s code=%ld"
+ "#InteractionDelegate: confirmation action branch=affirmative confirmed=%{bool}d"
+ "#InteractionDelegate: confirmation action branch=negative confirmed=%{bool}d"
+ "#IsolatedBackgroundPluginView: informHostOfViewResize not forwarded to host width=%f height=%f"
+ "#ItemView: failed to build prescribed action for simpleItem openAction errorDomain=%s errorCode=%ld"
+ "#PhotoPickerView failed to load photo library errorDomain=%s errorCode=%ld"
+ "#PhotoPickerView no photos selected, dismissing Siri"
+ "#PhotoPickerView photos picked, sending selection action selectionCount=%ld"
+ "#PhotosQuickLook Export failed for localId: %s: %s"
+ "#PhotosQuickLook asset not found for photo"
+ "#PhotosQuickLook configured macOS preview items count=%ld"
+ "#PhotosQuickLook export failed error=%s"
+ "#PhotosQuickLook exported asset cacheHit=%{bool}d"
+ "#PhotosQuickLook failed to purge cache errorDomain=%s errorCode=%ld"
+ "#PhotosQuickLook no photo resource found for asset"
+ "#PhotosQuickLook successfully exported asset"
+ "#PhotosUIGridView QuickLook tap ignored, data source not ready or preview index not found cloudIdIndex=%ld"
+ "#PhotosUIGridView accessing custom photo library libraryType=%s"
+ "#PhotosUIGridView asset not found for localId=%{private}s"
+ "#PhotosUIGridView cloud identifier not found in mappings index=%ld"
+ "#PhotosUIGridView displayedItemIdentifiers showing=%ld filteredFrom=%ld"
+ "#PhotosUIGridView failed to load a resolved image"
+ "#PhotosUIGridView failed to resolve cloud identifier index=%ld errorDomain=%s errorCode=%ld"
+ "#PhotosUIGridView initialized photoCount=%ld sourceCount=%ld fallbackImageCount=%ld"
+ "#PhotosUIGridView presenting QuickLook previewIndex=%ld"
+ "#PhotosUIGridView resolved identifiers success=%ld failed=%ld"
+ "#PhotosUIGridView resolved images loaded=%ld requested=%ld"
+ "#PhotosUIGridView showAllItems notification ignored, photoIds did not match"
+ "#PhotosUIGridView showAllItems notification matched, presenting tabbed grid"
+ "#PhotosUIGridView starting cloud identifier resolution identifierCount=%ld"
+ "#PhotosUIGridView using fallback local identifier index=%ld"
+ "#SectionHeaderView: dispatch via launchApp bundleId=%s"
+ "#SectionHeaderView: dispatch via prescribedAction action=%s"
+ "#SectionHeaderView: dispatch via showMore"
+ "#SectionHeaderView: failed to build prescribed action action=%s errorDomain=%s errorCode=%ld"
+ "#SectionHeaderView: tapped action=%s"
+ "#ShowMoreSheetView: dismissed by user"
+ "#SingleImageView: share button tapped"
+ "#SnippetServiceArchiveSource: archive fetch failed domain=%s code=%ld"
+ "#SnippetServiceArchiveSource: archive fetch succeeded"
+ "#SnippetServiceUIPlugin: rendering viewType=%s mode=%s idiom=%s"
+ "#SnippetServiceUIPlugin: unsupported snippet, no view for case=%s"
+ "#SnippetServiceUIPlugin: unsupported snippet, no view for case=properties"
+ "#StructuredInternalErrorView error view shown terminalErrorCount=%ld underlyingErrorCount=%ld"
+ "#SuggestionsView: suggestion tapped but no prompt available"
+ "#SuggestionsView: suggestion tapped promptLength=%ld"
+ "#SuggestionsView: text request dispatched success=%{bool}d"
+ "ButtonActionHandler: building openInApp (entityCriteria) action toolId=%{sensitive}s bundleId=%s entityCount=%ld"
+ "ButtonActionHandler: building openInApp action toolId=%{sensitive}s bundleId=%s hasEntityTarget=%{bool}d"
+ "ButtonActionHandler: building searchInApp action toolId=%{sensitive}s bundleId=%s criteriaCount=%ld"
+ "ButtonActionHandler: unable to parse bundleId actionType=openInApp toolId=%{sensitive}s"
+ "ButtonActionHandler: unable to parse bundleId actionType=openInAppWithEntities toolId=%{sensitive}s"
+ "ButtonActionHandler: unable to parse bundleId actionType=searchInApp toolId=%{sensitive}s"
+ "SFCardView Coordinator: SearchUICommandDelegate perform commandType=%s"
+ "SFCardView Coordinator: card section engaged"
+ "SFCardView Coordinator: executing ShowInAppStringSearchResultsIntent bundleId=%s query=%{sensitive}s"
+ "SFCardView Coordinator: failed ShowInAppStringSearchResultsIntent bundleId=%s domain=%s code=%ld"
+ "SFCardView Coordinator: finished ShowInAppStringSearchResultsIntent bundleId=%s"
+ "SFCardView Coordinator: macOS detached preferredContentSizeDidChange width=%f height=%f"
+ "SFCardView Coordinator: no actions conforming to ShowInAppStringSearchResultsIntent bundleId=%s"
+ "SFCardView Coordinator: performing IF action commandType=%s"
+ "SFCardView Coordinator: preferredContentSizeDidChange width=%f height=%f"
+ "SFCardView init: cardSectionTypes=%s idiom=%s"
+ "[SnippetNesting] %{public}s%{public}s"
+ "disambiguationDescriptor"
+ "domain"
+ "entityTarget"
+ "openAction"
+ "openInAppWithEntities"
+ "performCardOpenAction(_:)"
+ "prescribedAction"
+ "simpleItem (action: "
+ "snippetPlugin → "
+ "snippetPluginItem → "
+ "snippetPluginV2 → "
+ "→ plugin re-entry (depth "
- "#PhotoPickerView cancelled or no photos selected"
- "#PhotoPickerView failed to load photo library: %@"
- "#PhotoPickerView photos picked, sending selection action"
- "#PhotosQuickLook Asset not found for localId: %s"
- "#PhotosQuickLook Configured %ld macOS preview items"
- "#PhotosQuickLook Could not clean cached previews: %@"
- "#PhotosQuickLook Export failed for %{public}s: %{public}s"
- "#PhotosQuickLook No photo resource for localId: %s"
- "#PhotosQuickLook Successfully exported asset to: %s"
- "#PhotosQuickLook Using cached file for localId: %s"
- "#PhotosUIGridView Presenting QuickLook at index %ld for cloudId: %s"
- "#PhotosUIGridView QuickLook tap ignored — data source not ready or index not found for cloudId: %s"
- "#PhotosUIGridView accessing %ld photo libraries"
- "#PhotosUIGridView accessing custom photo library: %s"
- "#PhotosUIGridView asset not found for localId: %s"
- "#PhotosUIGridView calculated grid height: %f for %ld rows with %ld columns"
- "#PhotosUIGridView cloud identifier not found in mappings: %s"
- "#PhotosUIGridView custom library grid appeared with width: %f, height: %f"
- "#PhotosUIGridView disappeared, cleaning up presentation state"
- "#PhotosUIGridView displayedItemIdentifiers: showing %ld photos (filtered from %ld)"
- "#PhotosUIGridView failed to load resolved image for cloudId: %s"
- "#PhotosUIGridView failed to resolve cloud identifier: %s, error: %s, errorCode: %ld"
- "#PhotosUIGridView initialized with %ld photos from %ld sources, %ld fallback images"
- "#PhotosUIGridView loaded resolved image for cloudId: %s"
- "#PhotosUIGridView placeholder grid appeared with width: %f, height: %f"
- "#PhotosUIGridView received showAllItems notification, but they don't match our current photoIds"
- "#PhotosUIGridView received showAllItems notification, presenting tabbed grid"
- "#PhotosUIGridView resolved %ld identifiers, %ld failed"
- "#PhotosUIGridView starting cloud identifier resolution for %ld identifiers"
- "#PhotosUIGridView using fallback local identifier for: %s"
- "%s Action button tapped"
- "%s Actionable row tapped"
- "%s Building openInApp prescribed action for toolId: %s"
- "%s Building openInApp prescribed action for toolId: %s, entityCount: %ld"
- "%s Building searchInApp prescribed action for toolId: %s, criteria: %{sensitive}s"
- "%s Card row enagaged"
- "%s Performing IF action"
- "%s Primary button tapped"
- "%s Resetting throttle"
- "%s Secondary button tapped"
- "%s Throttling commands"
- "%s Throttling enabled, ignoring command"
- "%s Unable to parse bundleId from toolId: %s"
- "Album picked, sending disambiguation action with single value: %ld"
- "Executing ShowInAppStringSearchResultsIntent implementation on %s with query: %{sensitive}s"
- "Failed to build prescribed action: %@"
- "Failed to execute ShowInAppStringSearchResultsIntent implementation on %s: %@"
- "Finished executing ShowInAppStringSearchResultsIntent conformance on %s"
- "FlowToolsSnippetService"
- "IsolatedBackgroundPluginView informHostOfViewResize called with partial size: %fx%f, not forwarding to host"
- "No matching value selected with indices: %s"
- "SFCardView cardSections types: %s, idiom: %s"
- "SearchUICommandDelegate perform: %@"
- "Suggestion does not have a prompt in it"
- "Suggestion tapped"
- "Unable to find any actions conforming to ShowInAppStringSearchResultsIntent in %s"
- "buildOpenInAppPrescribedAction(toolId:bundleId:entityCriteria:)"
- "buildOpenInAppPrescribedAction(toolId:bundleId:entityTarget:)"
- "buildPrescribedAction(for:)"
- "buildSearchInAppPrescribedAction(toolId:bundleId:criteria:)"
- "com.apple.siri.flowtools.snippetservice"
- "interaction result: %{bool}d"
- "macOS - detached Task called in preferredContentSizeDidChange, cardViewController.preferredContentSize: %fx%f"
- "openActionableRowAction"
- "preferredContentSizeDidChange called, cardViewController.preferredContentSize: %fx%f"
- "secondaryAction()"
- "shouldHandleCardSectionEngagement(_:)"

```
