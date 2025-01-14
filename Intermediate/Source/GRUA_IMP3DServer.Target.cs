using UnrealBuildTool;

public class GRUA_IMP3DServerTarget : TargetRules
{
	public GRUA_IMP3DServerTarget(TargetInfo Target) : base(Target)
	{
		DefaultBuildSettings = BuildSettingsVersion.V3;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		Type = TargetType.Server;
		ExtraModuleNames.Add("GRUA_IMP3D");
	}
}
