## HomeUI

> `/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI`

```diff

 1166.5.10.1.1
-  __TEXT.__text: 0x6f9884
+  __TEXT.__text: 0x6fc770
   __TEXT.__auth_stubs: 0x7510
-  __TEXT.__objc_methlist: 0x4eecc
+  __TEXT.__objc_methlist: 0x4f2d4
   __TEXT.__const: 0x11218
   __TEXT.__dlopen_cstrs: 0x2a0
   __TEXT.__constg_swiftt: 0x91f0

   __TEXT.__swift5_assocty: 0xc20
   __TEXT.__swift5_proto: 0x794
   __TEXT.__swift5_types: 0x580
-  __TEXT.__cstring: 0x3e5c4
+  __TEXT.__cstring: 0x3e7b3
   __TEXT.__swift5_protos: 0x5c
-  __TEXT.__oslogstring: 0x26677
+  __TEXT.__oslogstring: 0x266ef
   __TEXT.__swift5_capture: 0x2b10
   __TEXT.__swift_as_entry: 0x2b4
   __TEXT.__swift_as_ret: 0x2d0
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x95a4
+  __TEXT.__gcc_except_tab: 0x95fc
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x1b8f0
+  __TEXT.__unwind_info: 0x1b9f8
   __TEXT.__eh_frame: 0xade4
-  __TEXT.__objc_classname: 0xf028
-  __TEXT.__objc_methname: 0xb32c7
-  __TEXT.__objc_methtype: 0x175ce
-  __TEXT.__objc_stubs: 0x6fa80
-  __DATA_CONST.__got: 0x6400
-  __DATA_CONST.__const: 0xee60
-  __DATA_CONST.__objc_classlist: 0x27b8
+  __TEXT.__objc_classname: 0xf117
+  __TEXT.__objc_methname: 0xb3b07
+  __TEXT.__objc_methtype: 0x17803
+  __TEXT.__objc_stubs: 0x6fd60
+  __DATA_CONST.__got: 0x6438
+  __DATA_CONST.__const: 0xeed8
+  __DATA_CONST.__objc_classlist: 0x27e0
   __DATA_CONST.__objc_catlist: 0x208
-  __DATA_CONST.__objc_protolist: 0x1270
+  __DATA_CONST.__objc_protolist: 0x1278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21b20
+  __DATA_CONST.__objc_selrefs: 0x21c78
   __DATA_CONST.__objc_protorefs: 0x6b8
-  __DATA_CONST.__objc_superrefs: 0x1e90
+  __DATA_CONST.__objc_superrefs: 0x1eb8
   __DATA_CONST.__objc_arraydata: 0x968
   __AUTH_CONST.__auth_got: 0x3a98
-  __AUTH_CONST.__const: 0x12c50
-  __AUTH_CONST.__cfstring: 0x221c0
-  __AUTH_CONST.__objc_const: 0x8c088
+  __AUTH_CONST.__const: 0x12c90
+  __AUTH_CONST.__cfstring: 0x22420
+  __AUTH_CONST.__objc_const: 0x8c908
   __AUTH_CONST.__objc_intobj: 0x1b30
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x578
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x1a750
+  __AUTH.__objc_data: 0x1a8e0
   __AUTH.__data: 0x3330
-  __DATA.__objc_ivar: 0x18ec
-  __DATA.__data: 0x102f8
+  __DATA.__objc_ivar: 0x1904
+  __DATA.__data: 0x10358
   __DATA.__objc_stublist: 0x40
   __DATA.__bss: 0xdaa8
   __DATA.__common: 0x218
-  __DATA_DIRTY.__objc_ivar: 0x3a98
+  __DATA_DIRTY.__objc_ivar: 0x3acc
   __DATA_DIRTY.__objc_data: 0x7dc0
   __DATA_DIRTY.__data: 0x1898
   __DATA_DIRTY.__common: 0xa0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4155363C-C0DF-3FCB-8412-D35509968772
-  Functions: 37991
-  Symbols:   88406
-  CStrings:  42561
+  UUID: 1E13681D-9033-3A4A-ABCB-7316EB6DAC9C
+  Functions: 38067
+  Symbols:   88649
+  CStrings:  42678
 
Symbols:
+ -[HUCalendarScrubberContainerViewController _fetchDatesWithClips]
+ -[HUCameraController diagnosticsController]
+ -[HUCameraController setDiagnosticsController:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController .cxx_destruct]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController cameraClip]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController eventTableView]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController initWithCameraClip:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController numberOfSectionsInTableView:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController setCameraClip:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController setEventTableView:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController tableView:cellForRowAtIndexPath:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController tableView:numberOfRowsInSection:]
+ -[HUDiagnosticsCameraClipSignificantEventsViewController viewDidLoad]
+ -[HUDiagnosticsCameraClipViewController .cxx_destruct]
+ -[HUDiagnosticsCameraClipViewController cameraClip]
+ -[HUDiagnosticsCameraClipViewController cameraProfile]
+ -[HUDiagnosticsCameraClipViewController eventTableView]
+ -[HUDiagnosticsCameraClipViewController initWithRecordingEvent:cameraProfile:]
+ -[HUDiagnosticsCameraClipViewController numberOfSectionsInTableView:]
+ -[HUDiagnosticsCameraClipViewController setCameraClip:]
+ -[HUDiagnosticsCameraClipViewController setCameraProfile:]
+ -[HUDiagnosticsCameraClipViewController setEventTableView:]
+ -[HUDiagnosticsCameraClipViewController tableView:cellForRowAtIndexPath:]
+ -[HUDiagnosticsCameraClipViewController tableView:didSelectRowAtIndexPath:]
+ -[HUDiagnosticsCameraClipViewController tableView:numberOfRowsInSection:]
+ -[HUDiagnosticsCameraClipViewController viewDidLoad]
+ -[HUDiagnosticsCameraPlayerController .cxx_destruct]
+ -[HUDiagnosticsCameraPlayerController cameraPlayerViewController]
+ -[HUDiagnosticsCameraPlayerController cameraProfile]
+ -[HUDiagnosticsCameraPlayerController clipScrubberDataSource]
+ -[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]
+ -[HUDiagnosticsCameraPlayerController diagnosticsView]
+ -[HUDiagnosticsCameraPlayerController dismissDetailsViewController]
+ -[HUDiagnosticsCameraPlayerController dismissDiagnosticDetails]
+ -[HUDiagnosticsCameraPlayerController displayDiagnosticDetails]
+ -[HUDiagnosticsCameraPlayerController displayTimelapseDetails]
+ -[HUDiagnosticsCameraPlayerController initWithCameraPlayerViewController:playbackEngine:clipScrubberDataSource:cameraProfile:]
+ -[HUDiagnosticsCameraPlayerController launchPlaybackEngineDiagnosticsView]
+ -[HUDiagnosticsCameraPlayerController playbackEngine]
+ -[HUDiagnosticsCameraPlayerController setCameraPlayerViewController:]
+ -[HUDiagnosticsCameraPlayerController setCameraProfile:]
+ -[HUDiagnosticsCameraPlayerController setClipScrubberDataSource:]
+ -[HUDiagnosticsCameraPlayerController setDiagnosticsView:]
+ -[HUDiagnosticsCameraPlayerController setPlaybackEngine:]
+ -[HUDiagnosticsCameraPlayerController updateWithPlaybackEngine:]
+ -[HUDiagnosticsCameraTimelineView .cxx_destruct]
+ -[HUDiagnosticsCameraTimelineView cameraStatusLabel]
+ -[HUDiagnosticsCameraTimelineView currentEventLabel]
+ -[HUDiagnosticsCameraTimelineView currentPositionLabel]
+ -[HUDiagnosticsCameraTimelineView currentTimelineStateLabel]
+ -[HUDiagnosticsCameraTimelineView initWithFrame:]
+ -[HUDiagnosticsCameraTimelineView moreButton]
+ -[HUDiagnosticsCameraTimelineView setCameraStatusLabel:]
+ -[HUDiagnosticsCameraTimelineView setCurrentEventLabel:]
+ -[HUDiagnosticsCameraTimelineView setCurrentPositionLabel:]
+ -[HUDiagnosticsCameraTimelineView setCurrentTimelineStateLabel:]
+ -[HUDiagnosticsCameraTimelineView setMoreButton:]
+ -[HUDiagnosticsCameraTimelineView updateWithPlaybackEngine:]
+ -[HUDiagnosticsReachabilityEventViewController .cxx_destruct]
+ -[HUDiagnosticsReachabilityEventViewController cameraProfile]
+ -[HUDiagnosticsReachabilityEventViewController container]
+ -[HUDiagnosticsReachabilityEventViewController eventTableView]
+ -[HUDiagnosticsReachabilityEventViewController initWithReachabilityEvent:cameraProfile:]
+ -[HUDiagnosticsReachabilityEventViewController numberOfSectionsInTableView:]
+ -[HUDiagnosticsReachabilityEventViewController setCameraProfile:]
+ -[HUDiagnosticsReachabilityEventViewController setContainer:]
+ -[HUDiagnosticsReachabilityEventViewController setEventTableView:]
+ -[HUDiagnosticsReachabilityEventViewController tableView:cellForRowAtIndexPath:]
+ -[HUDiagnosticsReachabilityEventViewController tableView:didSelectRowAtIndexPath:]
+ -[HUDiagnosticsReachabilityEventViewController tableView:numberOfRowsInSection:]
+ -[HUDiagnosticsReachabilityEventViewController viewDidLoad]
+ _HUCameraSignificantEventsBrowserCellIdentifier
+ _HUDiagnosticsHomeKitSettingsPath
+ _HUDiagnosticsHomeSettingsPath
+ _HUDiagnosticsReachabilityEventCellIdentifier
+ _HUDiagnosticsRecordingCellEventIdentifier
+ _OBJC_CLASS_$_AVURLAsset
+ _OBJC_CLASS_$_HUDiagnosticsCameraClipSignificantEventsViewController
+ _OBJC_CLASS_$_HUDiagnosticsCameraClipViewController
+ _OBJC_CLASS_$_HUDiagnosticsCameraPlayerController
+ _OBJC_CLASS_$_HUDiagnosticsCameraTimelineView
+ _OBJC_CLASS_$_HUDiagnosticsReachabilityEventViewController
+ _OBJC_CLASS_$_UIContextMenuInteraction
+ _OBJC_IVAR_$_HUCameraController._diagnosticsController
+ _OBJC_IVAR_$_HUDiagnosticsCameraPlayerController._cameraPlayerViewController
+ _OBJC_IVAR_$_HUDiagnosticsCameraPlayerController._cameraProfile
+ _OBJC_IVAR_$_HUDiagnosticsCameraPlayerController._clipScrubberDataSource
+ _OBJC_IVAR_$_HUDiagnosticsCameraPlayerController._diagnosticsView
+ _OBJC_IVAR_$_HUDiagnosticsCameraPlayerController._playbackEngine
+ _OBJC_METACLASS_$_HUDiagnosticsCameraClipSignificantEventsViewController
+ _OBJC_METACLASS_$_HUDiagnosticsCameraClipViewController
+ _OBJC_METACLASS_$_HUDiagnosticsCameraPlayerController
+ _OBJC_METACLASS_$_HUDiagnosticsCameraTimelineView
+ _OBJC_METACLASS_$_HUDiagnosticsReachabilityEventViewController
+ __OBJC_$_INSTANCE_METHODS_HUDiagnosticsCameraClipSignificantEventsViewController
+ __OBJC_$_INSTANCE_METHODS_HUDiagnosticsCameraClipViewController
+ __OBJC_$_INSTANCE_METHODS_HUDiagnosticsCameraPlayerController
+ __OBJC_$_INSTANCE_METHODS_HUDiagnosticsCameraTimelineView
+ __OBJC_$_INSTANCE_METHODS_HUDiagnosticsReachabilityEventViewController
+ __OBJC_$_INSTANCE_VARIABLES_HUDiagnosticsCameraClipSignificantEventsViewController
+ __OBJC_$_INSTANCE_VARIABLES_HUDiagnosticsCameraClipViewController
+ __OBJC_$_INSTANCE_VARIABLES_HUDiagnosticsCameraPlayerController
+ __OBJC_$_INSTANCE_VARIABLES_HUDiagnosticsCameraTimelineView
+ __OBJC_$_INSTANCE_VARIABLES_HUDiagnosticsReachabilityEventViewController
+ __OBJC_$_PROP_LIST_HUDiagnosticsCameraClipSignificantEventsViewController
+ __OBJC_$_PROP_LIST_HUDiagnosticsCameraClipViewController
+ __OBJC_$_PROP_LIST_HUDiagnosticsCameraPlayerController
+ __OBJC_$_PROP_LIST_HUDiagnosticsCameraTimelineView
+ __OBJC_$_PROP_LIST_HUDiagnosticsReachabilityEventViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIContextMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIContextMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIContextMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_REFS_UIContextMenuInteractionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HUDiagnosticsCameraClipSignificantEventsViewController
+ __OBJC_CLASS_PROTOCOLS_$_HUDiagnosticsCameraClipViewController
+ __OBJC_CLASS_PROTOCOLS_$_HUDiagnosticsCameraPlayerController
+ __OBJC_CLASS_PROTOCOLS_$_HUDiagnosticsReachabilityEventViewController
+ __OBJC_CLASS_RO_$_HUDiagnosticsCameraClipSignificantEventsViewController
+ __OBJC_CLASS_RO_$_HUDiagnosticsCameraClipViewController
+ __OBJC_CLASS_RO_$_HUDiagnosticsCameraPlayerController
+ __OBJC_CLASS_RO_$_HUDiagnosticsCameraTimelineView
+ __OBJC_CLASS_RO_$_HUDiagnosticsReachabilityEventViewController
+ __OBJC_LABEL_PROTOCOL_$_UIContextMenuInteractionDelegate
+ __OBJC_METACLASS_RO_$_HUDiagnosticsCameraClipSignificantEventsViewController
+ __OBJC_METACLASS_RO_$_HUDiagnosticsCameraClipViewController
+ __OBJC_METACLASS_RO_$_HUDiagnosticsCameraPlayerController
+ __OBJC_METACLASS_RO_$_HUDiagnosticsCameraTimelineView
+ __OBJC_METACLASS_RO_$_HUDiagnosticsReachabilityEventViewController
+ __OBJC_PROTOCOL_$_UIContextMenuInteractionDelegate
+ ___38-[HUCameraController cameraPickerMenu]_block_invoke.169
+ ___53-[HUClipScrubberViewController exportLocalClipAtURL:]_block_invoke.71
+ ___61-[HUCameraController _refreshClipCacheAndRefetchForClipUUID:]_block_invoke.154
+ ___64-[HUClipScrubberViewController exportCurrentClipWithCompletion:]_block_invoke.66
+ ___64-[HUClipScrubberViewController exportCurrentClipWithCompletion:]_block_invoke.67
+ ___65-[HUCalendarScrubberContainerViewController _fetchDatesWithClips]_block_invoke
+ ___86-[HUClipScrubberDataSource _snapshotForEvents:updatedIdentifiers:replacedIdentifiers:]_block_invoke.33
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_2
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_3
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_4
+ ___block_descriptor_40_e8_32w_e25_"UIMenu"16?0"NSArray"8lw32l8
+ ___block_descriptor_64_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.140
+ ___block_literal_global.274
+ _objc_msgSend$_fetchDatesWithClips
+ _objc_msgSend$cameraPlayerViewController
+ _objc_msgSend$cameraStatusLabel
+ _objc_msgSend$clipPlayer
+ _objc_msgSend$clipScrubberDataSource
+ _objc_msgSend$currentEventLabel
+ _objc_msgSend$currentPositionLabel
+ _objc_msgSend$currentTimelineStateLabel
+ _objc_msgSend$diagnosticsController
+ _objc_msgSend$diagnosticsView
+ _objc_msgSend$eventTableView
+ _objc_msgSend$fetchNewerEventsInAscendingOrder:
+ _objc_msgSend$initWithCameraPlayerViewController:playbackEngine:clipScrubberDataSource:cameraProfile:
+ _objc_msgSend$initWithReachabilityEvent:cameraProfile:
+ _objc_msgSend$initWithRecordingEvent:cameraProfile:
+ _objc_msgSend$launchPlaybackEngineDiagnosticsView
+ _objc_msgSend$resourceLoader
+ _objc_msgSend$setDiagnosticsController:
+ _objc_msgSend$setDiagnosticsView:
+ _objc_msgSend$shouldDisplayInternalViews
+ _objc_msgSend$startEvent
+ _objc_msgSend$targetFragmentDuration
+ _objc_msgSend$updateWithPlaybackEngine:
- ___38-[HUCameraController cameraPickerMenu]_block_invoke.167
- ___53-[HUClipScrubberViewController exportLocalClipAtURL:]_block_invoke.69
- ___61-[HUCameraController _refreshClipCacheAndRefetchForClipUUID:]_block_invoke.152
- ___64-[HUClipScrubberViewController exportCurrentClipWithCompletion:]_block_invoke.64
- ___64-[HUClipScrubberViewController exportCurrentClipWithCompletion:]_block_invoke.65
- ___86-[HUClipScrubberDataSource _snapshotForEvents:updatedIdentifiers:replacedIdentifiers:]_block_invoke.31
- ___block_literal_global.138
- ___block_literal_global.166
- ___block_literal_global.270
CStrings:
+ "!!\xf0\x92\xe1"
+ "%@: day %lu (%@ –\u00a0%@) contains clips? %{BOOL}d; %@"
+ "@\"HUDiagnosticsCameraPlayerController\""
+ "@\"HUDiagnosticsCameraTimelineView\""
+ "@\"UIContextMenuConfiguration\"40@0:8@\"UIContextMenuInteraction\"16{CGPoint=dd}24"
+ "@\"UITargetedPreview\"32@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24"
+ "@\"UITargetedPreview\"40@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24@\"<NSCopying>\"32"
+ "Can ask for feedback: %@"
+ "Complete: %@"
+ "Duration: %.2f"
+ "Event Details"
+ "HUCameraSignificantEventsBrowserCellIdentifier"
+ "HUDiagnosticsCameraClipSignificantEventsViewController"
+ "HUDiagnosticsCameraClipViewController"
+ "HUDiagnosticsCameraPlayerController"
+ "HUDiagnosticsCameraTimelineView"
+ "HUDiagnosticsReachabilityEventCellIdentifier"
+ "HUDiagnosticsReachabilityEventViewController"
+ "HUDiagnosticsRecordingCellEventIdentifier"
+ "Hide Inspector"
+ "Home Settings"
+ "HomeKit Settings"
+ "Show Inspector"
+ "Significant Events: %lu"
+ "Start Date: %@"
+ "T@\"AVPlayerViewController\",W,N,V_cameraPlayerViewController"
+ "T@\"HFCameraScrubberReachabilityEventContainer\",&,N,V_container"
+ "T@\"HUClipScrubberDataSource\",W,N,V_clipScrubberDataSource"
+ "T@\"HUDiagnosticsCameraPlayerController\",&,N,V_diagnosticsController"
+ "T@\"HUDiagnosticsCameraTimelineView\",&,N,V_diagnosticsView"
+ "T@\"UILabel\",&,N,V_cameraStatusLabel"
+ "T@\"UILabel\",&,N,V_currentEventLabel"
+ "T@\"UILabel\",&,N,V_currentPositionLabel"
+ "T@\"UILabel\",&,N,V_currentTimelineStateLabel"
+ "T@\"UITableView\",&,N,V_eventTableView"
+ "Target Fragment Duration: %.2f"
+ "UIContextMenuInteractionDelegate"
+ "UUID: %@"
+ "[INCREMENTAL FETCH] changing to live mode; fetching newest events"
+ "_cameraPlayerViewController"
+ "_cameraStatusLabel"
+ "_clipScrubberDataSource"
+ "_container"
+ "_currentEventLabel"
+ "_currentPositionLabel"
+ "_currentTimelineStateLabel"
+ "_diagnosticsController"
+ "_diagnosticsView"
+ "_eventTableView"
+ "_fetchDatesWithClips"
+ "cameraPlayerViewController"
+ "cameraStatusLabel"
+ "clipPlayer"
+ "clipScrubberDataSource"
+ "contextMenuInteraction:configuration:dismissalPreviewForItemWithIdentifier:"
+ "contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:"
+ "contextMenuInteraction:configurationForMenuAtLocation:"
+ "contextMenuInteraction:previewForDismissingMenuWithConfiguration:"
+ "contextMenuInteraction:previewForHighlightingMenuWithConfiguration:"
+ "contextMenuInteraction:willDisplayMenuForConfiguration:animator:"
+ "contextMenuInteraction:willEndForConfiguration:animator:"
+ "contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:"
+ "currentEventLabel"
+ "currentPositionLabel"
+ "currentTimelineStateLabel"
+ "diagnosticsController"
+ "diagnosticsView"
+ "dismissDetailsViewController"
+ "dismissDiagnosticDetails"
+ "displayDiagnosticDetails"
+ "displayTimelapseDetails"
+ "eventTableView"
+ "fetchNewerEventsInAscendingOrder:"
+ "hkc_incremental_fetch"
+ "initWithCameraPlayerViewController:playbackEngine:clipScrubberDataSource:cameraProfile:"
+ "initWithReachabilityEvent:cameraProfile:"
+ "initWithRecordingEvent:cameraProfile:"
+ "launchPlaybackEngineDiagnosticsView"
+ "magnifyingglass.circle"
+ "magnifyingglass.circle.fill"
+ "prefs:root=INTERNAL_SETTINGS&path=Home"
+ "prefs:root=INTERNAL_SETTINGS&path=HomeKit"
+ "resourceLoader"
+ "setCameraPlayerViewController:"
+ "setCameraStatusLabel:"
+ "setClipScrubberDataSource:"
+ "setContainer:"
+ "setCurrentEventLabel:"
+ "setCurrentPositionLabel:"
+ "setCurrentTimelineStateLabel:"
+ "setDiagnosticsController:"
+ "setDiagnosticsView:"
+ "setEventTableView:"
+ "shouldDisplayInternalViews"
+ "startEvent"
+ "targetFragmentDuration"
+ "updateWithPlaybackEngine:"
+ "v40@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionAnimating>\"32"
+ "v40@0:8@\"UIContextMenuInteraction\"16@\"UIContextMenuConfiguration\"24@\"<UIContextMenuInteractionCommitAnimating>\"32"
- "!!\xf0\x92\xd1"

```
