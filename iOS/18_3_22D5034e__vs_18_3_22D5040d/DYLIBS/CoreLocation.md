## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-2956.0.3.0.2
-  __TEXT.__text: 0x1bcf34
+2956.0.5.0.0
+  __TEXT.__text: 0x1bcfb0
   __TEXT.__auth_stubs: 0x1a10
   __TEXT.__objc_methlist: 0x9524
   __TEXT.__const: 0x4a05
   __TEXT.__gcc_except_tab: 0xcdf4
-  __TEXT.__oslogstring: 0x33c14
+  __TEXT.__oslogstring: 0x33c40
   __TEXT.__cstring: 0x201d1
   __TEXT.__ustring: 0x750
   __TEXT.__unwind_info: 0x53e0
CStrings:
+ "#clreg,#map,query,lla,%{sensitive}.6f,lon,%{sensitive}.6f,accuracy,%{sensitive}.2f"
+ "#clreg,#map,response,lla,%{sensitive}.6f,lon,%{sensitive}.6f,accuracy,%{sensitive}.2f,results,%{private}@"
+ "#clreg,fetchConfigForLocation,%{sensitive}.6f,%{sensitive}.6f,%{sensitive}.2f"
+ "#clreg,fetchInfoForLocation,%{sensitive}.6f,%{sensitive}.6f,%{sensitive}.2f"
+ "#clreg,fetchRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{sensitive}2.f,result,found"
+ "#clreg,fetchRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{sensitive}2.f,result,notFound"
+ "#clreg,findRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{sensitive}2.f,result,found"
+ "#clreg,findRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{sensitive}2.f,result,notFound"
+ "23:28:52"
+ "Dec 17 2024"
+ "{\"msg%{public}.0s\":\"#CLLocationManager invoking #delegate - request timeout\", \"self\":\"%{public}p\", \"delegate\":\"%{public}p\", \"selector\":%{public, location:escape_only}@, \"location\":%{sensitive, location:CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#CLLocationManager invoking #delegate\", \"self\":\"%{public}p\", \"delegate\":\"%{public}p\", \"selector\":%{public, location:escape_only}@, \"location\":%{sensitive, location:CLClientLocation}.*P, \"eventType\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#NullIsland Received a latitude or longitude from getLocationForBundleID that was exactly zero\", \"latIsNonzero\":%{public}hhd, \"lonIsNonzero\":%{public}hhd, \"hAcc\":\"%{public}f\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#NullIsland onClientEventLocation:forceMapMatching: got a latitude or longitude that was exactly zero\", \"latIsNonzero\":%{public}hhd, \"lonIsNonzero\":%{public}hhd, \"location\":%{sensitive, location:CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"No valid, cached location. Fetched from daemon\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"We have a valid, cached location. Fetching from internal state\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "#clreg,#map,query,lla,%{private}.6f,lon,%{private}.6f,accuracy,%{private}.2f"
- "#clreg,#map,response,lla,%{private}.6f,lon,%{private}.6f,accuracy,%{private}.2f,results,%{private}@"
- "#clreg,fetchConfigForLocation,%{private}.6f,%{private}.6f,%{private}.2f"
- "#clreg,fetchInfoForLocation,%{private}.6f,%{private}.6f,%{private}.2f"
- "#clreg,fetchRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{private}2.f,result,found"
- "#clreg,fetchRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{private}2.f,result,notFound"
- "#clreg,findRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{private}2.f,result,found"
- "#clreg,findRAEConfig,%{private}.6f,%{private}.6f,%{private}.2f,distToLocation,%{private}2.f,result,notFound"
- "19:37:50"
- "Dec 11 2024"
- "{\"msg%{public}.0s\":\"#CLLocationManager invoking #delegate - request timeout\", \"self\":\"%{public}p\", \"delegate\":\"%{public}p\", \"selector\":%{public, location:escape_only}@, \"location\":%{private, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#CLLocationManager invoking #delegate\", \"self\":\"%{public}p\", \"delegate\":\"%{public}p\", \"selector\":%{public, location:escape_only}@, \"location\":%{private, location:CLClientLocation}.*P, \"eventType\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#NullIsland Received a latitude or longitude from getLocationForBundleID that was exactly zero\", \"latIsNonzero\":%{public}hhd, \"lonIsNonzero\":%{public}hhd, \"hAcc\":\"%{public}f\", \"location\":%{private, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#NullIsland onClientEventLocation:forceMapMatching: got a latitude or longitude that was exactly zero\", \"latIsNonzero\":%{public}hhd, \"lonIsNonzero\":%{public}hhd, \"location\":%{private, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"No valid, cached location. Fetched from daemon\", \"location\":%{private, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"We have a valid, cached location. Fetching from internal state\", \"location\":%{private, location:CLClientLocation}.*P}"

```
