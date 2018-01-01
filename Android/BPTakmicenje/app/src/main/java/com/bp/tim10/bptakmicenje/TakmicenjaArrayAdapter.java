package com.bp.tim10.bptakmicenje;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.content.Context;
import android.widget.TextView;

import java.util.List;

/**
 * Created by ajlas on 02.01.2018..
 */

public class TakmicenjaArrayAdapter extends ArrayAdapter<CompetitionResponse> {
    private final Context context;
    private final List<CompetitionResponse> values;

    public TakmicenjaArrayAdapter(Context context, List<CompetitionResponse> values) {
        super(context, R.layout.activity_competitions_listview, values);
        this.context = context;
        this.values = values;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater inflater = (LayoutInflater) context
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View rowView = inflater.inflate(R.layout.activity_competitions_listview, parent, false);

        TextView mName = (TextView) rowView.findViewById(R.id.name);
        TextView mDescription = (TextView) rowView.findViewById(R.id.description);
        TextView mDate = (TextView) rowView.findViewById(R.id.date);

        mName.setText(values.get(position).name);
        mDescription.setText(values.get(position).description);
        mDate.setText(values.get(position).date.toString());

        return rowView;
    }
}
