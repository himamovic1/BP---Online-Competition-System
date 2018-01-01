package com.bp.tim10.bptakmicenje;

import com.google.gson.annotations.SerializedName;
import java.util.Date;

/**
 * Created by ajlas on 01.01.2018..
 */

public class CompetitionResponse {
    @SerializedName("date")
    public String date ;
    @SerializedName("field")
    public String description ;
    @SerializedName("field_id")
    public int id ;
    @SerializedName("name")
    public String name ;

}
