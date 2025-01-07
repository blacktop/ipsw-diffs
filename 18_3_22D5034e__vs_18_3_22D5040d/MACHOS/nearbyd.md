## nearbyd

> `/usr/libexec/nearbyd`

```diff

-460.0.21.0.0
-  __TEXT.__text: 0x4379ec
+462.0.1.0.0
+  __TEXT.__text: 0x4379d0
   __TEXT.__auth_stubs: 0x2910
   __TEXT.__objc_stubs: 0x111e0
   __TEXT.__init_offsets: 0x5e4
   __TEXT.__objc_methlist: 0x9bf4
-  __TEXT.__gcc_except_tab: 0x4794c
+  __TEXT.__gcc_except_tab: 0x47940
   __TEXT.__const: 0x2d56d0
-  __TEXT.__cstring: 0x3120c
+  __TEXT.__cstring: 0x3123c
   __TEXT.__objc_methname: 0x1a6c0
-  __TEXT.__oslogstring: 0x4cc47
+  __TEXT.__oslogstring: 0x4cc8d
   __TEXT.__objc_classname: 0x1864
   __TEXT.__objc_methtype: 0x1d094
   __TEXT.__swift5_typeref: 0x7d

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x17780
+  __TEXT.__unwind_info: 0x17788
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x14a0
   __DATA_CONST.__got: 0x980
   __DATA_CONST.__auth_ptr: 0x80
   __DATA_CONST.__const: 0x1fa68
-  __DATA_CONST.__cfstring: 0x11bc0
+  __DATA_CONST.__cfstring: 0x11be0
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x258
CStrings:
+ "#find-ses,Service processPeerLocationForPeer [%{private}@]: %{private}@. Location: %{sensitive}@"
+ "#find-ses,Service processSelfLocation [%{private}@]: %{sensitive}@"
+ "#find-ses,didUpdateLocations: %{sensitive}@"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/cb6e5652-bcd9-11ef-b66e-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "EnableFindingLocationInputProtobufLogging"
+ "regulatory,defaults,testLocation,lat,%{sensitive}.6f,lon,%{sensitive}.6f"
+ "regulatory,geo,loc,checkRegulatoryIso,geoServices,results,%{sensitive}@"
+ "regulatory,geo,loc,checkRegulatoryIso,lat,%{sensitive}.6f,lon,%{sensitive}.6f,unc,%{sensitive}.2f,isLastKnownLocation,%d,ts,%.2f,checkInterval,%.2f"
+ "regulatory,geo,loc,fOnRegulatoryRegion,%s,ll,%{sensitive}.6f,%{sensitive}.6f"
+ "regulatory,geo,loc,in isUnrestrictedGrid,%{sensitive}.6f,%{sensitive}.6f"
+ "regulatory,geo,loc,isTileAvailableBasedOnFile,%{sensitive}.6f,%{sensitive}.6f"
+ "regulatory,geo,loc,latlon,%{sensitive}u,lastValid,%d,lastLonLat,%{sensitive}u"
+ "regulatory,geof,default,site,name,%{sensitive}s,iso,%s,lat,%{sensitive}.6f,lon,%{sensitive}.6f,radius,%{sensitive}.2f"
+ "regulatory,geof,getLocationStatus,status,%{sensitive}s,site,lat,%{sensitive}.6f,lon,%{sensitive}.6f,radius,%{sensitive}.1f,loc,lat,%{sensitive}.6f,lon,%{sensitive}.6f,unc,%{sensitive}.1f,distance,%{sensitive}.2f"
+ "regulatory,geof,processLocation,%{sensitive}.6f,%{sensitive}.6f,%{sensitive}.2f,age,%.3f,logInterval,%.2f"
- "#find-ses,Service processPeerLocationForPeer [%{private}@]: %{private}@. Location: %{private}@"
- "#find-ses,Service processSelfLocation [%{private}@]: %{private}@"
- "#find-ses,[%s] Process event [%@]: %{private}@"
- "#find-ses,didUpdateLocations: %{private}@"
- "/AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/300e869f-b612-11ef-90fe-6efa4e70477e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "regulatory,defaults,testLocation,lat,%.6f,lon,%.6f"
- "regulatory,geo,loc,checkRegulatoryIso,geoServices,results,%{private}@"
- "regulatory,geo,loc,checkRegulatoryIso,lat,%{private}.6f,lon,%{private}.6f,unc,%{private}.2f,isLastKnownLocation,%{private}d,ts,%{private}.2f,checkInterval,%.2f"
- "regulatory,geo,loc,fOnRegulatoryRegion,%s,ll,%{private}.6f,%{private}.6f"
- "regulatory,geo,loc,in isUnrestrictedGrid,%.6f,%.6f"
- "regulatory,geo,loc,isTileAvailableBasedOnFile,%.6f,%.6f"
- "regulatory,geo,loc,latlon,%u,lastValid,%d,lastLonLat,%u"
- "regulatory,geof,default,site,name,%{private}s,iso,%s,lat,%{private}.6f,lon,%{private}.6f,radius,%{private}.2f"
- "regulatory,geof,getLocationStatus,status,%{private}s,site,lat,%{private}.6f,lon,%{private}.6f,radius,%{private}.1f,loc,lat,%{private}.6f,lon,%{private}.6f,unc,%{private}.1f,distance,%{private}.2f"
- "regulatory,geof,processLocation,%{private}.6f,%{private}.6f,%{private}.2f,age,%.3f,logInterval,%.2f"

```
