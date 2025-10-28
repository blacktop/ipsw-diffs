## HomeUI

> `/System/Library/PrivateFrameworks/HomeUI.framework/HomeUI`

```diff

 1119.2.10.1.3
-  __TEXT.__text: 0x6a60e0
+  __TEXT.__text: 0x6a8588
   __TEXT.__auth_stubs: 0x75f0
-  __TEXT.__objc_methlist: 0x4f30c
+  __TEXT.__objc_methlist: 0x4f704
   __TEXT.__const: 0x11500
   __TEXT.__dlopen_cstrs: 0x2a0
-  __TEXT.__cstring: 0x47d2d
+  __TEXT.__cstring: 0x47f06
   __TEXT.__swift5_typeref: 0xc76a
   __TEXT.__swift5_fieldmd: 0x4b18
   __TEXT.__constg_swiftt: 0x9000

   __TEXT.__swift_as_entry: 0x2a8
   __TEXT.__swift_as_ret: 0x2c8
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x9e78
+  __TEXT.__gcc_except_tab: 0x9efc
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x175a8
+  __TEXT.__unwind_info: 0x17658
   __TEXT.__eh_frame: 0xb0f0
-  __TEXT.__objc_classname: 0xcae4
-  __TEXT.__objc_methname: 0xae560
-  __TEXT.__objc_methtype: 0x15ddd
-  __TEXT.__objc_stubs: 0x6c520
-  __DATA_CONST.__got: 0x6380
-  __DATA_CONST.__const: 0xf168
-  __DATA_CONST.__objc_classlist: 0x27d0
+  __TEXT.__objc_classname: 0xcbd3
+  __TEXT.__objc_methname: 0xaed8b
+  __TEXT.__objc_methtype: 0x16012
+  __TEXT.__objc_stubs: 0x6c7c0
+  __DATA_CONST.__got: 0x63b8
+  __DATA_CONST.__const: 0xf1b8
+  __DATA_CONST.__objc_classlist: 0x27f8
   __DATA_CONST.__objc_catlist: 0x208
-  __DATA_CONST.__objc_protolist: 0x1270
+  __DATA_CONST.__objc_protolist: 0x1278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21c78
+  __DATA_CONST.__objc_selrefs: 0x21dc0
   __DATA_CONST.__objc_protorefs: 0x6b0
-  __DATA_CONST.__objc_superrefs: 0x1ea8
+  __DATA_CONST.__objc_superrefs: 0x1ed0
   __DATA_CONST.__objc_arraydata: 0x9c0
   __AUTH_CONST.__auth_got: 0x3b08
-  __AUTH_CONST.__const: 0x12a80
-  __AUTH_CONST.__cfstring: 0x22d40
-  __AUTH_CONST.__objc_const: 0x8c6b0
+  __AUTH_CONST.__const: 0x12ac0
+  __AUTH_CONST.__cfstring: 0x22fa0
+  __AUTH_CONST.__objc_const: 0x8cf30
   __AUTH_CONST.__objc_intobj: 0x1cc8
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x5c8
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x1a738
+  __AUTH.__objc_data: 0x1a8c8
   __AUTH.__data: 0x3260
-  __DATA.__objc_ivar: 0x186c
-  __DATA.__data: 0x10628
+  __DATA.__objc_ivar: 0x1884
+  __DATA.__data: 0x10688
   __DATA.__objc_stublist: 0x40
   __DATA.__bss: 0xd868
   __DATA.__common: 0x250
-  __DATA_DIRTY.__objc_ivar: 0x3b7c
+  __DATA_DIRTY.__objc_ivar: 0x3bb0
   __DATA_DIRTY.__objc_data: 0x7e00
   __DATA_DIRTY.__data: 0x1680
   __DATA_DIRTY.__common: 0xa0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 000204FA-C746-3E8E-B6C2-5EA6DF376598
-  Functions: 38181
-  Symbols:   88243
-  CStrings:  43233
+  UUID: 03F81B4C-8075-30DD-B3D3-4F3BD55ACDC8
+  Functions: 38255
+  Symbols:   88479
+  CStrings:  43345
 
Symbols:
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
+ ___38-[HUCameraController cameraPickerMenu]_block_invoke.165
+ ___61-[HUCameraController _refreshClipCacheAndRefetchForClipUUID:]_block_invoke.150
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_2
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_3
+ ___93-[HUDiagnosticsCameraPlayerController contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke_4
+ ___block_descriptor_40_e8_32w_e25_"UIMenu"16?0"NSArray"8lw32l8
+ ___block_literal_global.164
+ ___block_literal_global.270
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
- ___38-[HUCameraController cameraPickerMenu]_block_invoke.163
- ___61-[HUCameraController _refreshClipCacheAndRefetchForClipUUID:]_block_invoke.148
CStrings:
+ "!!\xf0\x92\xe1"
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
