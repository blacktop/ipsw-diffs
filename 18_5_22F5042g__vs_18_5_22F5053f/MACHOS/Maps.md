## Maps

> `/private/var/staged_system_apps/Maps.app/Maps`

```diff

-2864.35.3.6.2
-  __TEXT.__text: 0xd98448
+2864.35.3.6.3
+  __TEXT.__text: 0xd98500
   __TEXT.__auth_stubs: 0x8560
   __TEXT.__objc_stubs: 0xf6c20
   __TEXT.__objc_methlist: 0xbf554
   __TEXT.__const: 0x19008
   __TEXT.__dlopen_cstrs: 0x191
-  __TEXT.__cstring: 0x99556
+  __TEXT.__cstring: 0x995c4
   __TEXT.__objc_methname: 0x17522b
   __TEXT.__swift5_typeref: 0x1b2b0
   __TEXT.__constg_swiftt: 0x91a4

   __TEXT.__objc_methtype: 0x39e88
   __TEXT.__swift_as_entry: 0x4f0
   __TEXT.__swift_as_ret: 0x4fc
-  __TEXT.__oslogstring: 0x6034b
+  __TEXT.__oslogstring: 0x6056c
   __TEXT.__swift5_mpenum: 0x70
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__gcc_except_tab: 0x1f528
+  __TEXT.__gcc_except_tab: 0x1f4dc
   __TEXT.__ustring: 0x17a4
   __TEXT.__unwind_info: 0x33488
   __TEXT.__eh_frame: 0x9b04
   __DATA_CONST.__auth_got: 0x42c8
   __DATA_CONST.__got: 0x58c8
-  __DATA_CONST.__auth_ptr: 0x2298
-  __DATA_CONST.__const: 0x4dd48
+  __DATA_CONST.__auth_ptr: 0x1f98
+  __DATA_CONST.__const: 0x4dda8
   __DATA_CONST.__cfstring: 0x74fa0
   __DATA_CONST.__objc_classlist: 0x5ef8
   __DATA_CONST.__objc_catlist: 0x638

   __DATA.__objc_data: 0x43518
   __DATA.__data: 0x2ced8
   __DATA.__objc_stublist: 0x10
-  __DATA.__bss: 0x18e08
+  __DATA.__bss: 0x18e18
   __DATA.__common: 0x11e0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 76162
+  Functions: 76164
   Symbols:   5453
-  CStrings:  92709
+  CStrings:  92725
 
CStrings:
+ "-[CarRouteSelectionController _selectRouteAtIndex:]"
+ "CarRouteSelectionController.m"
+ "[%{public}p] Attempted to select LAR with MNTrafficIncidentAlertType_Blockage, ignoring"
+ "[%{public}p] Attempted to select alternate route which is already selected"
+ "[%{public}p] Could not find route with index %lu in configuration: %@"
+ "[%{public}p] Denying label marker selection because it is not of type route ETA: %@"
+ "[%{public}p] Didn't find a focused alternate route item for knob press."
+ "[%{public}p] Failed to find a route associated with focused route item in routeAnnotationsController"
+ "[%{public}p] Failed to find selected label marker route index for config: %@"
+ "[%{public}p] Found selected label marker route at index: %lu"
+ "[%{public}p] Handling knob selection"
+ "[%{public}p] Initializing for scene: %@"
+ "[%{public}p] Knob press has wrong type: %ld; ignoring"
+ "[%{public}p] Not rebuilding alternate route items. Reson: active: %@, routesCount: %lu"
+ "[%{public}p] Rebuilding alternate route items. Alternate routes count: %lu"
+ "[%{public}p] Selected route from routeAnnotationsConfiguration was not found in currentRouteCollection"
+ "[%{public}p] Setting active: %@"
+ "[%{public}p] Tapped map view at point: %@"
+ "[%{public}p] Tried to insert _routeItemContainingView, but self.mapView is nil."
+ "[%{public}p] Trying to select route at index: %lu"
+ "[%{public}p] Updating alternate route focus items: %@"
+ "[%{public}p] Updating focused route index %lu -> %lu"
+ "[%{public}p] Updating session %@ -> %@"
+ "[%{public}p] didTapMapView:atPoint: %@. selectedRoute.routeIndex: %lu"
+ "[%{public}p] didTapMapView:atPoint: alternate routes on config were not enabled; ignoring call: %@"
+ "[%{public}p] handleKnobPress: will attempt an alternate route with index: %lu"
- "[%{public}@] CarRouteSelectionController attempted to select LAR with MNTrafficIncidentAlertType_Blockage, ignoring."
- "[%{public}@] CarRouteSelectionController attempted to select alternate route which is already selected."
- "[%{public}@] CarRouteSelectionController: Didn't find a focused alternate route item for knob press."
- "[%{public}@] CarRouteSelectionController: Failed to find a route associated with focused route item in routeAnnotationsController."
- "[%{public}@] CarRouteSelectionController: Not rebuilding alternate route items. Reson: active: %@, routesCount: %lu"
- "[%{public}@] CarRouteSelectionController: Rebuilding alternate route items. Alternate routes count: %lu"
- "[%{public}@] CarRouteSelectionController: setting active: %@"
- "[%{public}@] CarRouteSelectionController: tried to insert _routeItemContainingView, but self.mapView is nil."
- "[%{public}@] didTapMapView:atPoint: %@. selectedRoute.routeIndex: %lu"
- "[%{public}@] didTapMapView:atPoint: alternate routes were not enabled, ignoring call"
- "[%{public}@] handleKnobPress: will attempt an alternate route with index: %lu"

```
