using UnrealBuildTool;

public class GRUA_IMP3DClientTarget : TargetRules
{
	public GRUA_IMP3DClientTarget(TargetInfo Target) : base(Target)
	{
		DefaultBuildSettings = BuildSettingsVersion.V3;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		Type = TargetType.Client;
		ExtraModuleNames.Add("GRUA_IMP3D");
	}
}
